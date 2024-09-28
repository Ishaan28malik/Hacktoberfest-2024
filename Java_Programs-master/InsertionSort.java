package tugas2;
public class InsertionSort {
    PremierLeague leagues[] = new PremierLeague[20];
    int id;
    
    void tambah(PremierLeague epl){
        if(id < leagues.length){
            leagues[id] = epl;
            id++;
        }else{
            System.out.println("Data klub sudah penuh!");
        }
    }
    void tampilAll(){
        for(PremierLeague epl : leagues){
            epl.tampil();
           System.out.println("---------------------------------------------------");
        }
    }
    void insertionSort(boolean asc){
        for(int i=1; i<leagues.length; i++){
            PremierLeague temp = leagues[i];
            int j=i;
            if(asc){
                while(j>0 && leagues[j-1].points > temp.points){
                    leagues[j] = leagues[j-1];
                    j--;
                }
            }else{
                while(j>0 && leagues[j-1].points < temp.points){
                    leagues[j] = leagues[j-1];
                    j--;
                }
            }
            leagues[j] = temp;
        }
    }
}
