import sys
import mysql.connector
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

class LibraryApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("우리 동네 도서관 관리 프로그램")
        self.resize(500, 300)

        # 1. 메인 위젯 및 레이아웃 설정
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # 2. 테이블 위젯 생성
        self.table = QTableWidget(0, 3)  # 0행 3열
        self.table.setHorizontalHeaderLabels(["ID", "제목", "저자"])
        self.layout.addWidget(self.table)

        # 3. 데이터 로드 및 출력
        self.load_data()

    def load_data(self):
        # DB 연결 및 데이터 가져오기
        conn = mysql.connector.connect(host='localhost', user='root', password='11111', database='library_db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        rows = cursor.fetchall()
        conn.close()

        # 4. 가져온 데이터를 테이블에 삽입
        self.table.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, val in enumerate(row):
                self.table.setItem(i, j, QTableWidgetItem(str(val)))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LibraryApp()
    window.show()
    sys.exit(app.exec())