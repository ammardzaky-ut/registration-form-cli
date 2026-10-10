import random

class EmployeeModel:
    """Kelas khusus untuk menyimpan struktur data karyawan (Data Model)."""
    def __init__(self, first_name: str, last_name: str, address: str, age: int, experience: int, position: str, salary: float):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.address = address
        self.age = age
        self.experience = experience
        self.position = position.upper()
        self.salary = salary
        self.employee_code = self._generate_employee_code()

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def _generate_employee_code(self) -> str:
        """Membuat kode unik secara otomatis (Encapsulation logic)."""
        dept = self.position[:3] if len(self.position) >= 3 else "GEN"
        initials = (self.first_name[0] + self.last_name[0]) if self.last_name else self.first_name[:2]
        unique_id = random.randint(100, 999)
        return f"{dept}-2026-{initials}-{unique_id}"

class RegistrationController:
    """Kelas untuk mengatur logika registrasi dan input pengguna."""
    
    @staticmethod
    def prompt_integer(message: str) -> int:
        """Helper method untuk mencegah aplikasi crash saat user memasukkan huruf."""
        while True:
            try:
                return int(input(message))
            except ValueError:
                print("Error: Harap masukkan angka yang valid.")
                
    @staticmethod
    def prompt_float(message: str) -> float:
        """Helper method untuk angka desimal/gaji."""
        while True:
            try:
                return float(input(message))
            except ValueError:
                print("Error: Harap masukkan nominal yang valid.")

    def run_registration(self):
        print("=== Employee Registration Form ===\n")
        
        # Pengumpulan Data
        f_name = input("First Name: ").strip()
        l_name = input("Last Name: ").strip()
        
        addr_main = input("Address: ").strip()
        addr_extra = input("Apartment/Unit (Optional): ").strip()
        final_address = f"{addr_main}, {addr_extra}" if addr_extra else addr_main
        
        age = self.prompt_integer("Age: ")
        exp = self.prompt_integer("Years of Experience: ")
        pos = input("Job Position (e.g. Developer, Sales): ").strip()
        salary = self.prompt_float("Expected Salary ($): ")
        
        # Membuat instansiasi Data Model
        employee = EmployeeModel(f_name, l_name, final_address, age, exp, pos, salary)
        
        self._display_summary(employee)

    def _display_summary(self, emp: EmployeeModel):
        print("\n" + "="*30)
        print("   REGISTRATION SUCCESSFUL")
        print("="*30)
        print(f"Employee ID : {emp.employee_code}")
        print(f"Name        : {emp.full_name}")
        print(f"Address     : {emp.address}")
        print(f"Profile     : {emp.age} years old | {emp.experience} yrs exp.")
        print(f"Role        : {emp.position} | Salary: ${emp.salary:,.2f}")
        
        # Ekstraksi kode (Slicing) untuk menunjukkan pemahaman manipulasi string
        print("-" * 30)
        print(f"System Parsed Info:")
        print(f"- Dept Code : {emp.employee_code[:3]}")
        print(f"- Join Year : {emp.employee_code[4:8]}")

if __name__ == "__main__":
    app = RegistrationController()
    app.run_registration()