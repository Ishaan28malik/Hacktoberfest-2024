package pertemuan_1.tugas.peminjaman;

public class Peminjaman {
  public String id;
  public Member member;
  public Peminjam peminjam;
  public VideoGame game;
  public int lamaPinjam;
  public int totalBayar;

  public void addPeminjamanMem(String id, Member member, VideoGame game, int lamaPinjam, int totalBayar) {
    this.id = id;
    this.member = member;
    this.game = game;
    this.lamaPinjam = lamaPinjam;
    this.totalBayar = totalBayar;
  }

  public void addPeminjamanPmj(String id, Peminjam peminjam, VideoGame game, int lamaPinjam, int totalBayar) {
    this.id = id;
    this.peminjam = peminjam;
    this.game = game;
    this.lamaPinjam = lamaPinjam;
    this.totalBayar = totalBayar;
  }

  public void printPeminjaman() {
    if(member != null) {
      System.out.printf("| %-7s | %-7s | %-10s | %-15s | Rp. %-8d | %4d hari | Rp. %-8d | %-10s |\n",id, member.id, member.nama, game.nama, game.hargaSewa, lamaPinjam, totalBayar," Gratis +2 jam");
    } else {
      System.out.printf("| %-7s | %-7s | %-10s | %-15s | Rp. %-8d | %4d hari | Rp. %-8d | %-10s |\n",id, "Non Mem", peminjam.nama, game.nama, game.hargaSewa, lamaPinjam, totalBayar, "     ---      ");
    }
  }
  
}
