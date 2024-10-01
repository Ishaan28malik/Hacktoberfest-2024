package pertemuan_1.tugas.peminjaman;

import java.util.InputMismatchException;
import java.util.Scanner;

public class Main {
  static Scanner scanner = new Scanner(System.in);
  private static void printGames(VideoGame[] games) {
    System.out.println("\t\t\t\t DAFTAR GAME");
    System.out.println("-----------------------------------------------------------------------------");
    System.out.printf("%-7s | %-20s | %-17s | %4s | %-12s    |\n", "Id", "Nama Game", "Genre", "Stok", "Harga Sewa");
    System.out.println("-----------------------------------------------------------------------------");
    for (VideoGame game : games) {
      if (game.id == null) {
        continue;
      } else {
        game.printGame();
      }
    }
  }

  private static void printMembers(Member[] members) {
    System.out.println("\t\t\t\t\t DAFTAR MEMBER");
    System.out.println("--------------------------------------------------------------------------------------------");
    System.out.printf("%-8s | %-10s | %-20s | %-10s | %-15s | %-12s |\n", "Id", "Jenis", "Nama", "Alamat", "Email", "No Telp");
    System.out.println("--------------------------------------------------------------------------------------------");
    for (Member member : members) {
      if (member.id == null) {
        continue;
      } else {
        member.printMember();
      }
    }
  }

  private static void printPeminjamans(Peminjaman[] peminjamans) {
    System.out.println("\t\t\t\t\t DAFTAR PEMINJAMAN");
    System.out.println("---------------------------------------------------------------------------------------------------------------");
    System.out.printf("| %-7s | %-7s | %-10s | %-15s | %-8s | %-4s | %-8s | %-10s |\n", "Id", "Id Mem", "Nama","Game", "Harga Sewa  ", "Lama Pnjm", "Total bayar ", "Bonus         ");
    System.out.println("---------------------------------------------------------------------------------------------------------------");
    int countPeminjaman = countPeminjaman(peminjamans);
    // System.out.println(countPeminjaman);
    int i = 0;
    for (Peminjaman peminjaman : peminjamans) {
      if (countPeminjaman != 0) {
        peminjaman.printPeminjaman();
        i++;
      } else {
        break;
      }

      if (i == countPeminjaman) break;
    }
  }

  private static void instanceVidGame(VideoGame[] obj) {
    for (int i = 0; i < obj.length; i++){
      obj[i] = new VideoGame();
    }
  }

  private static void instanceMember(Member[] obj) {
    for (int i = 0; i < obj.length; i++){
      obj[i] = new Member();
    }
  }

  private static void instancePeminjaman(Peminjaman[] obj) {
    for (int i = 0; i < obj.length; i++) {
      obj[i] = new Peminjaman();
    }
  }

  private static void menu() {
    System.out.println("Yooo Geminkkk | Penyewaan Game PC");
    System.out.println("1. Peminjaman");
    System.out.println("2. Cek Daftar Game");
    System.out.println("3. Cek Daftar Member");
    System.out.println("4. Cek Daftar Peminjaman");
    System.out.println("5. Keluar");
    System.out.print("Input[1-5]>> ");
  }

  private static int cekIdMember(Member[] members, String idMem) {
    int index = 0;
    int countMem = countMem(members);
    for (Member member : members) {
      if(member.id == null) {
        break;
      } else {
        if(member.id.equals(idMem)) {
          break;
        } else {
          if(index == countMem - 1) {
            return 404;
          }
        }
        index++;
      }
    }
    return index;
  }

  private static int cekIdGame(VideoGame[] games, String idGame) {
    int index = 0;
    int countGame = 0;
    for (VideoGame game : games) {
      if(game.id != null) {
        if(game.id.equals(idGame)) {
          break;
        } else {
          if(countGame == games.length -1) {
            return 404;
          }
        }
        countGame++;
        index++;
      } else {
        break;
      }
    }
    return index;
  }

  private static int countMem(Member[] members) {
    int countResult = 0;
    for (Member member : members) {
      if(member.id == null) {
        break;
      } else {
        countResult++;
      }
    }
    return countResult;
  }

  private static int countPeminjaman(Peminjaman[] peminjamans) {
    int countResult = 0;
    for (Peminjaman peminjaman : peminjamans) {
      if(peminjaman.member != null || peminjaman.peminjam != null) {
        countResult++;
      } else {
        break;
      }
    }
    return countResult;
  }

  private static Peminjam isiDataDiri() {
    System.out.print("Input nama peminjam: ");
    String pmjName = scanner.nextLine();
    System.out.print("Input alamat peminjam: ");
    String pmjAddr = scanner.nextLine();
    System.out.print("Input email peminjam: ");
    String pmjEmail = scanner.nextLine();
    System.out.print("Input No Telp: ");
    String pmjPhone = scanner.nextLine();
   
    //create peminjam obj
    Peminjam pmjTemp = new Peminjam();
    pmjTemp.setPeminjam(pmjName, pmjAddr, pmjEmail, pmjPhone);

    return pmjTemp;
  }
  
  public static void main(String[] args) {
    
    // define array of obj
    VideoGame[] games = new VideoGame[10];
    Member[] members = new Member[10];
    Peminjaman[] peminjamans = new Peminjaman[10];

    // instansiai arr of obj games
    instanceVidGame(games);

    //instansiasi arr of obj member
    instanceMember(members);

    //instansiasi arr of obj peminjaman
    instancePeminjaman(peminjamans);

    // Set Games Data
    games[0].setGame("gim-01", "Dota 2", "Moba", 20, 40000);
    games[1].setGame("gim-02", "GTA V", "Action", 10, 25000);
    games[2].setGame("gim-03", "CSGO", "FPS", 8, 35000);
    games[3].setGame("gim-04", "PUBG", "Battle Royale", 14, 40000);
    games[4].setGame("gim-05", "Assassins Creed", "Action", 13, 45000);
    games[5].setGame("gim-06", "League of Legends", "Moba", 10, 30000);
    games[6].setGame("gim-07", "Call of Duty", "FPS", 16, 45000);
    games[7].setGame("gim-08", "Resident Evil", "Survival", 5, 50000);
    games[8].setGame("gim-09", "Watch dogs", "Action", 9, 45000);
    games[9].setGame("gim-10", "MineCraft", "Survival", 0, 20000); // end of set games

    //Set member's Data
    members[0].joinMember("mem-01", "Karbitan", "Taufik", "Kediri", "opik@mail.com", "0821312xxxx");
    
    int input = 0;
    do {      
      // validasi inputan from usr
      try {
        menu();
        input = scanner.nextInt();   
        scanner.nextLine();
      } catch(InputMismatchException e) {
        System.out.println("Input tidak valid [Note: 'input hanya boleh angka']");
        input = 404;
        scanner.nextLine();
      }

      System.out.println();

      switch (input) {
        //menu peminjaman
        case 1:
          System.out.print("Apakah pelanggan seorang member?[y/t] ");
          char inpMember = scanner.next().charAt(0);
          scanner.nextLine();
          if (String.valueOf(inpMember).equalsIgnoreCase("y")) {
            System.out.print("Input Id member: ");
            String inpIdMem = scanner.nextLine();

            int idMemFound = cekIdMember(members, inpIdMem);

            if(idMemFound != 404) {
              //tampilkan list game
              printGames(games);
              System.out.println();
              //isi form peminjaman
              System.out.print("Input Id game: ");
              String inpIdGame = scanner.nextLine();

              int idGame = cekIdGame(games, inpIdGame);

              if(idGame != 404 && games[idGame].stok >= 1) {
                try {
                  System.out.print("Input lama peminjaman[hari]: ");
                  int inpLamaPnjm = scanner.nextInt();
                  scanner.nextLine();
                  //kurangi stok
                  games[idGame].stok--;
                  //count rows peminjaman
                  int countPeminjaman = countPeminjaman(peminjamans);
                  // System.out.print(countPeminjaman);
                  //set peminjaman data[member]
                  String ids = "pmj-0" + String.valueOf(countPeminjaman);
                  int totBay = games[idGame].hargaSewa * inpLamaPnjm;

                  peminjamans[countPeminjaman].addPeminjamanMem(ids, members[idMemFound], games[idGame], inpLamaPnjm, totBay);

                } catch(InputMismatchException E) {
                  System.out.println("Input tidak valid [Note: 'input hanya boleh angka']");
                  scanner.nextLine();
                }
              } else if(idGame == 404) {
                System.out.println("Game dengan id " + inpIdGame + " TIDAK DITEMUKAN!");
              } else {
                System.out.println("Stok game habis!");
              }
              // printMembers(members);
            } else {
              System.out.println("member dengan id " + inpIdMem + " tidak ditemukan");
            }
          } else {
            System.out.println("Apakah pelanggan ingin mendaftar member?[y/n] *meminjam tanpa register member bisa");
            System.out.print(">> ");
            char inpJoinMem = scanner.next().charAt(0);
            scanner.nextLine();

            if(String.valueOf(inpJoinMem).equalsIgnoreCase("y")) {
              //execute func to register memb
              Peminjam pmjTemp = new Peminjam();
              pmjTemp = isiDataDiri();

              int countMemb = countMem(members);
              int index = 0;
              if(countMemb > 0) {
                index = countMemb;
              }

              System.out.print("Input jenis member: ");
              String jenisMem = scanner.nextLine();

              String id = "mem-0" + String.valueOf(countMemb + 1);

              members[index].joinMember(id, jenisMem, pmjTemp.nama, pmjTemp.alamat, pmjTemp.email, pmjTemp.noTelp);
              System.out.println("Register success");
          
            } else {
              //show the list of gim
              printGames(games);
              System.out.print("Input id game: ");
              String inpIdGame = scanner.nextLine();

              //check id game
              int idGame = cekIdGame(games, inpIdGame);

              if(idGame != 404 && games[idGame].stok >= 1) {
                try {
                   //isi identitas
                  Peminjam pmjTemp = new Peminjam();
                  pmjTemp  = isiDataDiri();

                  System.out.print("Input lama peminjaman[hari]: ");
                  int inpLamaPnjm = scanner.nextInt();
                  scanner.nextLine();
              
                  //kurangi stok
                  games[idGame].stok--;
                  //count rows peminjaman
                  int countPeminjaman = countPeminjaman(peminjamans);
                  // System.out.print(countPeminjaman);
                  //set peminjaman data[member]
                  String ids = "pmj-0" + String.valueOf(countPeminjaman);
                  int totBay = games[idGame].hargaSewa * inpLamaPnjm;

                  peminjamans[countPeminjaman].addPeminjamanPmj(ids, pmjTemp, games[idGame], inpLamaPnjm, totBay);

                } catch (InputMismatchException e) {
                  System.out.println("Invalid input");
                }
              }

            }
          }
        break;
        //cek daftar game
        case 2:
          printGames(games);
        break;
        //cek daftar member
        case 3:
          printMembers(members);
        break;
        case 4:
          printPeminjamans(peminjamans);
        break;
        //exit
        case 5:
        break;
      }
      System.out.println();      
    } while((input > 0 && input < 5) || input == 404);

  }
}
