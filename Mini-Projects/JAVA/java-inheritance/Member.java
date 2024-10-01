package pertemuan_1.tugas.peminjaman;

public class Member extends Peminjam {
  public String id;
  public String jenisMember;

  public void joinMember(String id, String jenisMember, String nama, String alamat, String email, String noTelp) {
    this.id = id;
    this.jenisMember = jenisMember;
    super.nama = nama;
    super.alamat = alamat;
    super.email = email;
    super.noTelp = noTelp;
  }

  public void printMember() {
    System.out.printf("%-8s | %-10s | %-20s | %-10s | %-15s | %-12s |\n", id, jenisMember, super.nama, super.alamat, super.email, super.noTelp);
  }
}
