package pertemuan_1.tugas.peminjaman;

public class VideoGame {
  public String id;
  public String nama;
  public String genre;
  public int stok;
  public int hargaSewa;

  public void setGame(String id, String nama, String genre, int stok, int hargaSewa) {
    this.id = id;
    this.nama = nama;
    this.genre = genre;
    this.stok = stok;
    this.hargaSewa = hargaSewa;
  }

  public void printGame() {
    System.out.printf("%-7s | %-20s | %-17s | %4d | Rp.%-12d |\n", id, nama, genre, stok, hargaSewa);
  }
}
