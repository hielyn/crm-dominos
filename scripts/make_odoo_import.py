"""
make_odoo_import.py - Tao file CSV theo dinh dang IMPORT cua Odoo 17 tu dataset trong data/.
Chay TU THU MUC GOC REPO (sau khi da co data/*.csv):  python scripts/make_odoo_import.py
Ket qua: data/odoo_import/ gom 5 file, import theo thu tu 0 -> 1 -> 2 -> 3a -> 3b.
(chua kiem chung tren Odoo that - xem data/README.md)
Cac cot chua dua vao Odoo vi truong tuy chinh x_dom_* cua A chua chot:
ngay_sinh, so_thich_mon, kenh_chinh, persona, hang, diem, kenh/cua_hang/edt/adt/giao_tre cua don.
"""
import csv, os

SRC, OUT = "data", "data/odoo_import"
os.makedirs(OUT, exist_ok=True)


def rd(name):
    with open(f"{SRC}/{name}.csv", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def save(name, header, rows):
    with open(f"{OUT}/{name}", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)


P, C, O, L = rd("products"), rd("customers"), rd("orders"), rd("order_lines")

# 0. Nhom san pham (product.category) - external id dom_cat_NN
cats = {}
for p in P:
    cats.setdefault(p["nhom"], f"dom_cat_{len(cats) + 1:02d}")
save("0_product_categories.csv", ["id", "name"], [(v, k) for k, v in cats.items()])

# 1. San pham (product.template)
save("1_products.csv",
     ["id", "name", "detailed_type", "list_price", "standard_price", "default_code", "categ_id/id"],
     [(f"dom_{p['ma_sp'].lower()}", p["ten_sp"], "consu", p["gia_ban"], p["chi_phi_nguyen_lieu"],
       p["ma_sp"], cats[p["nhom"]]) for p in P])

# 2. Khach hang (res.partner); ma_kh luu o truong Reference (ref)
rows = []
for c in C:
    street, street2, city = [x.strip() for x in c["dia_chi"].split(",")]
    rows.append((f"dom_{c['ma_kh'].lower()}", c["ho_ten"], c["ma_kh"], c["sdt"], c["email"],
                 street, street2, city, "Vietnam", 1))
save("2_partners.csv",
     ["id", "name", "ref", "phone", "email", "street", "street2", "city", "country_id", "customer_rank"], rows)

# 3. Don ban (sale.order + order_line). Dong dau cua moi don co day du cot don, cac dong sau de trong.
lines_by = {}
for l in L:
    lines_by.setdefault(l["ma_don"], []).append(l)
HEADER = ["id", "name", "partner_id/id", "date_order", "state",
          "order_line/product_id", "order_line/name", "order_line/product_uom_qty", "order_line/price_unit"]


def build(orders):
    out = []
    for o in orders:
        for k, l in enumerate(lines_by[o["ma_don"]]):
            head = ([f"dom_{o['ma_don'].lower()}", o["ma_don"], f"dom_{o['ma_kh'].lower()}",
                     o["ngay_dat"], "sale"] if k == 0 else [""] * 5)
            out.append(head + [l["ma_sp"], l["ten_sp"], l["so_luong"], l["don_gia"]])  # ma_sp = Internal Reference (default_code)
    return out


save("3a_sale_orders_TEST5.csv", HEADER, build(O[:5]))   # 5 don dau: thu truoc
save("3b_sale_orders_REST.csv", HEADER, build(O[5:]))    # phan con lai (KHONG trung 5 don thu)
print("Da tao data/odoo_import/:", sorted(os.listdir(OUT)))
