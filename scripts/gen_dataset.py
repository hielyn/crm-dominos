"""
gen_dataset.py (v2) - Sinh dataset cho do an CRM Domino's Pizza (vai tro B).
Khop 3 persona trong persona.docx: S1 Hoc sinh-sinh vien, S2 Nhan vien van phong, S3 Gia dinh va nhom.
Chi dung thu vien chuan Python 3.8+.   Chay:  python gen_dataset.py
Ket qua: thu muc data/ gom 8 file CSV (UTF-8). Seed co dinh -> chay lai ra cung ket qua.
Toan bo du lieu la GIA LAP (ten, SDT, email @example.com).
Moi tham so hanh vi ben duoi (kenh, gio dat, ngay dat, gio hang) la GIA DINH cua nhom,
khong phai so lieu thuc cua Domino's Viet Nam (xem persona.docx muc 0).
"""
import csv, os, random
from datetime import date, timedelta

random.seed(2026)
TODAY = date(2026, 11, 10)
START = date(2026, 6, 1)          # don trai ~5 thang -> co cua so 30-60 ngay
EDT = 45                          # [CAN XAC NHAN] dinh nghia EDT/ADT chua thong nhat
OUT = "data"
os.makedirs(OUT, exist_ok=True)


def save(name, header, rows):
    with open(f"{OUT}/{name}", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)


# ---------------- 1. SAN PHAM (32) ----------------
RAW = [
    ("Pizza", "Pizza Phô Mai Truyền Thống", 129000), ("Pizza", "Pizza Pepperoni", 149000),
    ("Pizza", "Pizza Hải Sản Xốt Pesto", 189000), ("Pizza", "Pizza Thập Cẩm Thượng Hạng", 179000),
    ("Pizza", "Pizza Bò Xốt BBQ", 169000), ("Pizza", "Pizza Gà Nướng Dứa", 159000),
    ("Pizza", "Pizza Xúc Xích Ý", 149000), ("Pizza", "Pizza Rau Củ", 129000),
    ("Pizza", "Pizza Tôm Xốt Kem", 189000), ("Pizza", "Pizza Phô Mai Hải Sản", 199000),
    ("Pizza", "Pizza Bò Mexico", 169000), ("Pizza", "Pizza Giăm Bông Dứa", 139000),
    ("Món phụ", "Mì Ý Bò Bằm", 79000), ("Món phụ", "Mì Ý Hải Sản", 89000),
    ("Món phụ", "Khoai Tây Chiên", 39000), ("Món phụ", "Bánh Mì Bơ Tỏi", 45000),
    ("Món phụ", "Salad Caesar", 59000), ("Món phụ", "Xúc Xích Nướng", 55000),
    ("Gà", "Cánh Gà Nướng BBQ 6 miếng", 89000), ("Gà", "Gà Viên Chiên Giòn", 69000),
    ("Gà", "Đùi Gà Rán", 79000), ("Gà", "Cánh Gà Cay 6 miếng", 89000),
    ("Đồ uống", "Pepsi lon", 19000), ("Đồ uống", "7Up lon", 19000),
    ("Đồ uống", "Trà Đào", 35000), ("Đồ uống", "Nước suối", 12000),
    ("Tráng miệng", "Bánh Trứng Tart", 35000), ("Tráng miệng", "Kem Ly Vani", 29000),
    ("Combo", "Combo Cá Nhân", 119000), ("Combo", "Combo Bạn Bè 2 Người", 289000),
    ("Combo", "Combo Gia Đình 4 Người", 459000), ("Combo", "Combo Văn Phòng 6 Người", 599000),
]
products = []
for i, (g, n, p) in enumerate(RAW, 1):
    cost = int(round(p * random.uniform(0.30, 0.42), -2))
    products.append((f"SP{i:03d}", n, g, p, cost))
save("products.csv", ["ma_sp", "ten_sp", "nhom", "gia_ban", "chi_phi_nguyen_lieu"], products)
by_group = {}
for p in products:
    by_group.setdefault(p[2], []).append(p)
pizza_names = [p[1] for p in by_group["Pizza"]] + [p[1] for p in by_group["Gà"]]

# ---------------- 2. THAM SO PERSONA (GIA DINH, theo persona.docx) ----------------
PLABEL = {"S1": "S1 Học sinh - sinh viên", "S2": "S2 Nhân viên văn phòng", "S3": "S3 Gia đình và nhóm"}
# tuoi persona: S1 16-24 (dung 18-24 de tranh du lieu nguoi chua thanh nien), S2 22-39, S3 28-45
BIRTH = {"S1": (2002, 2008), "S2": (1987, 2004), "S3": (1981, 1998)}
CHANNELS = ["Website", "App", "Hotline", "POS"]
CHW = {"S1": [20, 50, 10, 20],    # uu tien app
       "S2": [35, 25, 30, 10],    # giao hang, dien thoai/may tinh
       "S3": [10, 40, 10, 40]}    # app hoac mang di (POS)
GW = {  # trong so nhom mon
    "S1": {"Pizza": 3, "Món phụ": 3, "Gà": 3, "Đồ uống": 3, "Tráng miệng": 2, "Combo": 1},
    "S2": {"Pizza": 3, "Món phụ": 2, "Gà": 2, "Đồ uống": 3, "Tráng miệng": 1, "Combo": 3},
    "S3": {"Pizza": 4, "Món phụ": 3, "Gà": 3, "Đồ uống": 2, "Tráng miệng": 2, "Combo": 4},
}
LINES = {"S1": (1, 3), "S2": (1, 3), "S3": (2, 5)}          # so dong/don: S3 don lon
REUSE = {"S1": 0.25, "S2": 0.60, "S3": 0.30}                # xac suat dat lai gio quen (S2 cao nhat)
COMBO_OK = {"S1": ["Combo Cá Nhân", "Combo Bạn Bè 2 Người"],
            "S2": ["Combo Cá Nhân", "Combo Bạn Bè 2 Người", "Combo Văn Phòng 6 Người"],
            "S3": ["Combo Bạn Bè 2 Người", "Combo Gia Đình 4 Người"]}


def snap(d, persona):
    """S3 dat cuoi tuan; S2 dat ngay di lam (lui ve ngay hop le gan nhat)."""
    if persona == "S3":
        while d.weekday() < 5:
            d -= timedelta(days=1)
    elif persona == "S2":
        while d.weekday() >= 5:
            d -= timedelta(days=1)
    return d


def pick_hour(persona):
    if persona == "S2":
        return random.choice([11, 12, 12, 13]) if random.random() < 0.8 else random.randint(17, 20)
    if persona == "S1":
        return random.randint(16, 21)
    return random.randint(11, 20)


def make_basket(persona):
    gw = GW[persona]
    chosen = {}
    for _ in range(random.randint(*LINES[persona])):
        g = random.choices(list(gw), weights=list(gw.values()))[0]
        pool = by_group[g]
        if g == "Combo":
            pool = [p for p in pool if p[1] in COMBO_OK[persona]]
        if persona == "S1":   # nhay gia: uu tien mon re
            p = random.choices(pool, weights=[1 / x[3] for x in pool])[0]
        else:
            p = random.choice(pool)
        q = random.choices([1, 2], [0.7, 0.3] if persona == "S3" else [0.85, 0.15])[0]
        chosen[p[0]] = (p, q)
    return list(chosen.values())


# ---------------- 3. KHACH HANG (60) ----------------
HO = ["Nguyễn", "Trần", "Lê", "Phạm", "Hoàng", "Huỳnh", "Võ", "Đặng", "Bùi", "Đỗ"]
DEM_NAM = ["Văn", "Minh", "Quốc", "Hữu", "Đức", "Gia"]
DEM_NU = ["Thị", "Ngọc", "Thu", "Phương", "Khánh", "Mai"]
TEN_NAM = ["Anh", "Bình", "Cường", "Dũng", "Hải", "Khoa", "Long", "Nam", "Phúc", "Tuấn", "Hưng", "Sơn"]
TEN_NU = ["An", "Chi", "Dung", "Giang", "Hà", "Hương", "Lan", "Linh", "My", "Ngân", "Thảo", "Trang"]
STREETS = ["Nguyễn Huệ", "Lê Lợi", "Điện Biên Phủ", "Phạm Văn Đồng", "Nguyễn Thị Thập",
           "Quang Trung", "Võ Văn Ngân", "Cách Mạng Tháng 8", "Lê Văn Việt", "Hoàng Diệu"]
DISTRICTS = ["Quận 1", "Quận 3", "Quận 7", "Quận 10", "Thủ Đức", "Gò Vấp", "Bình Thạnh", "Phú Nhuận"]
STORES = ["CH Quận 1", "CH Quận 7", "CH Thủ Đức", "CH Gò Vấp"]  # [ĐỀ XUẤT]

PERSONAS = ["S1"] * 20 + ["S2"] * 20 + ["S3"] * 20
PROFILES = ["VIP"] * 8 + ["Thường xuyên"] * 16 + ["Mới"] * 14 + ["At-risk"] * 12 + ["Không mua lại"] * 10
random.shuffle(PERSONAS)
random.shuffle(PROFILES)
# (ngay_tu, ngay_den, so_don_min, so_don_max): so ngay tu don cuoi den TODAY
RULE = {"VIP": (1, 14, 8, 12), "Thường xuyên": (5, 28, 4, 7), "Mới": (3, 25, 1, 2),
        "At-risk": (31, 60, 2, 5), "Không mua lại": (61, 130, 1, 3)}


def make_name():
    if random.random() < 0.55:
        return f"{random.choice(HO)} {random.choice(DEM_NU)} {random.choice(TEN_NU)}"
    return f"{random.choice(HO)} {random.choice(DEM_NAM)} {random.choice(TEN_NAM)}"


def gen_dates(profile, persona):
    a1, a2, n1, n2 = RULE[profile]
    while True:  # don cuoi nam dung khoang ngay cua profile va dung loai ngay cua persona
        d = TODAY - timedelta(days=random.randint(a1, a2))
        if snap(d, persona) == d:
            break
    n = random.randint(n1, n2)
    gap = (4, 10) if profile == "VIP" else (7, 25)
    ds, cur = {d}, d
    while len(ds) < n:
        cur = cur - timedelta(days=random.randint(*gap))
        s = snap(cur, persona)
        if s < START:
            break
        ds.add(s)
    return sorted(ds)


customers, raw_orders, usual, pmap = [], [], {}, {}
for i, (persona, prof) in enumerate(zip(PERSONAS, PROFILES), 1):
    ma = f"KH{i:03d}"
    pmap[ma] = persona
    usual[ma] = make_basket(persona)
    ds = gen_dates(prof, persona)
    reg = ds[0] if prof == "Mới" else ds[0] - timedelta(days=random.randint(0, 90))
    y1, y2 = BIRTH[persona]
    bday = date(random.randint(y1, y2), random.randint(1, 12), random.randint(1, 28))
    main_ch = random.choices(CHANNELS, weights=CHW[persona])[0]
    home = random.choice(STORES)
    addr = f"{random.randint(1, 300)} {random.choice(STREETS)}, {random.choice(DISTRICTS)}, TP.HCM"
    customers.append([ma, make_name(), f"09000{i:05d}", f"{ma.lower()}@example.com",
                      bday.isoformat(), addr, random.choice(pizza_names), main_ch,
                      reg.isoformat(), PLABEL[persona], "", "", prof])
    for d in ds:
        ch = main_ch if random.random() < 0.7 else random.choices(CHANNELS, weights=CHW[persona])[0]
        st = home if random.random() < 0.85 else random.choice(STORES)
        raw_orders.append((d, ma, ch, st, persona))
save("customers.csv",
     ["ma_kh", "ho_ten", "sdt", "email", "ngay_sinh", "dia_chi", "so_thich_mon", "kenh_chinh",
      "ngay_dang_ky", "persona", "hang", "diem", "nhom_mo_phong_de_kiem_tra_RFM"], customers)

# ---------------- 4. DON HANG + CHI TIET ----------------
raw_orders.sort(key=lambda x: x[0])
orders, lines = [], []
for j, (d, ma, kenh, store, persona) in enumerate(raw_orders, 1):
    mdh = f"DH{j:04d}"
    basket = usual[ma] if random.random() < REUSE[persona] else make_basket(persona)
    total = 0
    for p, q in basket:
        lines.append((mdh, p[0], p[1], q, p[3], q * p[3]))
        total += q * p[3]
    if kenh == "POS":
        edt, adt, late = "", "", ""
    else:
        adt = random.randint(46, 75) if random.random() < 0.15 else random.randint(20, 45)
        edt, late = EDT, int(adt > EDT)
    ts = f"{d.isoformat()} {pick_hour(persona):02d}:{random.randint(0, 59):02d}:00"
    orders.append((mdh, ma, ts, kenh, store, total, edt, adt, late))
save("orders.csv", ["ma_don", "ma_kh", "ngay_dat", "kenh", "cua_hang", "tong_tien",
                    "edt_phut", "adt_phut", "giao_tre"], orders)
save("order_lines.csv", ["ma_don", "ma_sp", "ten_sp", "so_luong", "don_gia", "thanh_tien"], lines)

# ---------------- 5. TICKET (18) ----------------
late_o = [o for o in orders if o[8] == 1]
other_o = [o for o in orders if o[8] != 1 and o[3] != "POS"]
pick = random.sample(late_o, min(12, len(late_o))) + random.sample(other_o, 6)
pick.sort(key=lambda o: o[2])
OTHER_T = ["Sai món", "Chất lượng món", "Thái độ nhân viên", "Thanh toán"]
tickets = []
for k, o in enumerate(pick, 1):
    is_late = o[8] == 1
    loai = "Giao trễ" if is_late and random.random() < 0.8 else random.choice(OTHER_T)
    csat = random.choice([2, 3, 3, 4]) if is_late else random.choice([3, 4, 4, 5])
    tickets.append((f"TK{k:03d}", o[1], o[0], loai, o[2][:10],
                    round(random.uniform(0.5, 36), 1), csat))
save("tickets.csv", ["ma_ticket", "ma_kh", "ma_don", "loai", "ngay_tao", "gio_xu_ly", "csat"], tickets)

# ---------------- 6. LEAD B2B (16) ----------------
COMP = ["Công ty TNHH Ánh Dương", "Công ty CP Phần mềm Sao Mai", "Công ty TNHH Thương mại Hải Đăng",
        "Ngân hàng Chi nhánh Bến Thành", "Trường THPT Lê Quý Đôn", "Công ty CP Xây dựng Phú Gia",
        "Công ty TNHH Logistics Nam Việt", "Studio Thiết kế Bản Sắc", "Công ty CP Dược Hưng Thịnh",
        "Công ty TNHH Du lịch Biển Xanh", "Trung tâm Anh ngữ Global Star", "Công ty CP Điện tử Viễn Đông",
        "Công ty TNHH Quảng cáo Màu Sắc", "Phòng khám Đa khoa An Tâm", "Công ty CP Thực phẩm Vạn Lộc",
        "Công ty TNHH Tư vấn Khởi Nghiệp"]
NEED = ["Tiệc công ty", "Sinh nhật", "Họp mặt cuối năm", "Team building"]
LOST = ["Giá cao", "Chọn đối thủ", "Hủy sự kiện", "Không liên lạc được"]
leads = []
for i, c in enumerate(COMP, 1):
    n = random.randint(20, 150)
    kq = random.choices(["Thắng", "Thua", "Đang xử lý"], [35, 35, 30])[0]
    d = START + timedelta(days=random.randint(0, (TODAY - START).days - 5))
    leads.append((f"LD{i:03d}", c, make_name(), f"lienhe{i:02d}@example.com", f"08000{i:05d}",
                  random.choice(NEED), n, n * random.randint(90, 150) * 1000,
                  random.choice(["Form WordPress", "Hotline", "Giới thiệu"]), d.isoformat(),
                  kq, random.choice(LOST) if kq == "Thua" else ""))
leads.sort(key=lambda r: r[9])
leads = [(f"LD{i:03d}",) + r[1:] for i, r in enumerate(leads, 1)]
save("leads_b2b.csv", ["ma_lead", "cong_ty", "nguoi_lien_he", "email", "sdt", "nhu_cau", "so_nguoi",
                       "gia_tri_du_kien", "nguon", "ngay_tao", "ket_qua", "ly_do_that_bai"], leads)

# ---------------- 7. GIO BO (12) ----------------
carts = []
ids = random.sample([c[0] for c in customers], 8)
for k in range(12):
    d = TODAY - timedelta(days=random.randint(3, 60))
    ma_kh = ids[k] if k < 8 else ""
    email = next(c[3] for c in customers if c[0] == ma_kh) if ma_kh else f"khach_vang_lai{k - 7}@example.com"
    n = random.randint(1, 4)
    val = sum(random.choice(products)[3] for _ in range(n))
    sent = random.random() < 0.8
    back = sent and random.random() < 0.35
    carts.append((d, ma_kh, email, n, val, "Có" if sent else "Không", "Có" if back else "Không"))
carts.sort(key=lambda r: r[0])
save("abandoned_carts.csv", ["ma_gio", "ma_kh", "email", "ngay", "so_mon", "gia_tri_gio",
                             "da_gui_email_nhac", "da_quay_lai_mua"],
     [(f"AB{i:03d}", c[1], c[2], c[0].isoformat(), c[3], c[4], c[5], c[6]) for i, c in enumerate(carts, 1)])

# ---------------- 8. THONG KE EMAIL (8 chien dich) ----------------
CAMP = [("Welcome T6", "Welcome", "2026-06-10"), ("Sinh nhật T7", "Sinh nhật", "2026-07-15"),
        ("Newsletter T7", "Newsletter", "2026-07-30"), ("At-risk đợt 1", "At-risk", "2026-08-20"),
        ("Newsletter T9", "Newsletter", "2026-09-10"), ("Nhắc giỏ hàng đợt 1", "Giỏ bỏ", "2026-09-25"),
        ("At-risk đợt 2", "At-risk", "2026-10-15"), ("Newsletter T11", "Newsletter", "2026-11-03")]
em = []
for k, (n, t, d) in enumerate(CAMP, 1):
    sent = random.randint(25, 58)
    op = int(sent * random.uniform(0.25, 0.55))
    cl = int(op * random.uniform(0.15, 0.40))
    od = int(cl * random.uniform(0.20, 0.60))
    em.append((f"EM{k:02d}", n, t, d, sent, op, cl, od))
save("email_stats.csv", ["ma_chien_dich", "ten", "loai", "ngay_gui", "so_gui", "so_mo", "so_click",
                         "so_dat_don"], em)

# ---------------- KIEM TRA NHANH ----------------
last = {}
for o in orders:
    last[o[1]] = max(last.get(o[1], ""), o[2][:10])
b = {"<=30 ngay": 0, "31-60 ngay (at-risk)": 0, ">60 ngay": 0}
for v in last.values():
    days = (TODAY - date.fromisoformat(v)).days
    b["<=30 ngay" if days <= 30 else "31-60 ngay (at-risk)" if days <= 60 else ">60 ngay"] += 1
print("Khach:", len(customers), "| San pham:", len(products), "| Don:", len(orders),
      "| Dong don:", len(lines))
print("Ticket:", len(tickets), "| Lead:", len(leads), "| Gio bo:", len(carts), "| Chien dich email:", len(em))
print("Don tre:", sum(1 for o in orders if o[8] == 1), "| Don theo kenh:",
      {c: sum(1 for o in orders if o[3] == c) for c in CHANNELS})
print("Khoang cach tu don cuoi den", TODAY, ":", b)
print("Don dau tien:", orders[0][2][:10], "| Don cuoi:", orders[-1][2][:10])
for s in ("S1", "S2", "S3"):
    os_ = [o for o in orders if pmap[o[1]] == s]
    wk = sum(1 for o in os_ if date.fromisoformat(o[2][:10]).weekday() >= 5)
    lunch = sum(1 for o in os_ if 11 <= int(o[2][11:13]) <= 13)
    print(f"{PLABEL[s]}: {len(os_)} don | gia tri TB {sum(o[5] for o in os_) // len(os_):,} VND"
          f" | cuoi tuan {wk * 100 // len(os_)}% | 11-13h {lunch * 100 // len(os_)}%")