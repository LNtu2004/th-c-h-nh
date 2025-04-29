import pandas as pd

class MoneyTime:
    def __init__(self):
        self.gia_tien = {
            "Xe đạp": 2000,
            "Xe máy": 5000,
            "Xe điện": 3500,
            "Ô tô": 10000
        }

    def cap_nhat_gia(self, loai_xe, gia_moi):
        self.gia_tien[loai_xe] = gia_moi

    def lay_gia(self, loai_xe):
        return self.gia_tien.get(loai_xe, 0)


class InfoXe:
    def __init__(self, loai_xe, chu_xe, gio_gui, bien_so=None):
        self.loai_xe = loai_xe
        self.chu_xe = chu_xe
        self.gio_gui = gio_gui
        self.bien_so = bien_so

    def tinh_tien(self, bang_gia: MoneyTime):
        return self.gio_gui * bang_gia.lay_gia(self.loai_xe)

    def to_dict(self, bang_gia: MoneyTime):
        return {
            "Chủ xe": self.chu_xe,
            "Loại xe": self.loai_xe,
            "Giờ gửi": self.gio_gui,
            "Biển số": self.bien_so or "",
            "Thành tiền": self.tinh_tien(bang_gia)
        }


class BaiGiuXe:
    def __init__(self):
        self.ds_xe = []
        self.bang_gia = MoneyTime()

    def them_xe(self, xe: InfoXe):
        self.ds_xe.append(xe)

    def xoa_xe(self, chu_xe):
        self.ds_xe = [xe for xe in self.ds_xe if xe.chu_xe != chu_xe]

    def sua_xe(self, chu_xe, loai_xe=None, gio_gui=None, bien_so=None):
        for xe in self.ds_xe:
            if xe.chu_xe == chu_xe:
                if loai_xe: xe.loai_xe = loai_xe
                if gio_gui: xe.gio_gui = gio_gui
                if bien_so: xe.bien_so = bien_so

    def xuat_ds_gui_tren_20k(self):
        return [xe for xe in self.ds_xe if xe.tinh_tien(self.bang_gia) > 20000]

    def ghi_file_excel(self, ten_file="danh_sach_gui_xe.xlsx"):
        data = [xe.to_dict(self.bang_gia) for xe in self.ds_xe]
        df = pd.DataFrame(data)
        df.to_excel(ten_file, index=False)
        print(f"✅ Đã ghi dữ liệu vào file: {ten_file}")


# Ví dụ sử dụng
bai_giu = BaiGiuXe()

# Thêm xe
bai_giu.them_xe(InfoXe("Xe đạp", "Nguyễn Văn A", 3))
bai_giu.them_xe(InfoXe("Xe máy", "Trần Thị B", 5, "29B1-12345"))
bai_giu.them_xe(InfoXe("Ô tô", "Lê Văn C", 2, "30A-99999"))

# Cập nhật bảng giá (nếu muốn)
bai_giu.bang_gia.cap_nhat_gia("Xe điện", 4000)

# In danh sách gửi xe > 20k
print("\n🔍 Danh sách xe gửi trên 20k:")
for xe in bai_giu.xuat_ds_gui_tren_20k():
    print(f"- {xe.chu_xe}: {xe.tinh_tien(bai_giu.bang_gia)} VNĐ")

# Ghi dữ liệu vào file Excel
bai_giu.ghi_file_excel()
