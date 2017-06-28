public static void main(String[] ar) throws SQLException
 {
     
     try {
         
        ServerSocket ss1 = null;
        ServerSocket ss2 = null;
 
        Thread acceptor1;
        Thread acceptor2;
 
        Socket cs1=null;
        Socket cs2=null;
 
        ExecutorService output;
        final int OUTPUT_THREADS=5;
 
        p1=Collections.synchronizedSet(new HashSet<Socket>());
        p2=Collections.synchronizedSet(new HashSet<Socket>());
          
         try {
                 ss1 = new ServerSocket(80);
                 ss2 = new ServerSocket(4211);
              } catch (IOException ex) {}
        
          cs1=ss1.accept();
          cs2=ss2.accept();
           
          acceptor2=new Connect_To(cs2);
          acceptor1=new Connect_To(cs1);
  
          Thread t1=new Thread(acceptor1,"80");
          Thread t2=new Thread(acceptor2,"4211");
 
          output=Executors.newFixedThreadPool(OUTPUT_THREADS);
           
           t1.start();     
           t2.start();
       
        } catch (Exception ex) { }
            
      
}
