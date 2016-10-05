/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package lab1_matrix;
import java.util.Random;


/**
 *
 * @author ihtisham
 */
public class Lab1_Matrix {

    /**
     * @param args the command line arguments
     */
    
    public static void randomPopulate(int[][] a){
        //populates the matrix with random values; upper bound is 10
        int a_rows = a.length;
        int a_col = a[0].length;
        
        Random randomValue = new Random();

        for(int i=0;i<a_rows;i++){
            for(int j=0;j<a_col;j++){
                int randomInt = randomValue.nextInt(10);
                a[i][j] = randomInt;
            }
        }
        
        

    }
    
    // prints the matrix
    public static void printMatrix(int[][] a){
        for(int i=0;i<a.length;i++){
            for(int j=0;j<a[0].length;j++){
                System.out.println(a[i][j]);
            }
            System.out.println("\n");
        }
    }
    
   // Matrix multiplication through iterative method
    public static int[][] iter(int[][] a, int[][] b){
        
        int a_rows = a.length;
        int b_rows = b.length;
        int a_col = a[0].length;
        int b_col = b[0].length;
        
        int[][] result = new int[a_rows][b_col];
        
        // checks if rows of a and columns of b are equal for multiplication to continue
        if(a_col!=b_rows){
            System.out.println("Multiplication not possible");
        }
        else{
              for(int i=0;i<a_rows;i++){
                  for(int j=0;j<b_col;j++){ 
                    for(int k=0;k<a_col;k++){
                        result[i][j] += a[i][k] * b[k][j];
                    }
                  }   
            }
        }
        return result;

    }
    
    // the strassen method could only be implemented on 2x2 matrices
    public static int[][] strassen(int[][] a,int[][] b){
       int n = a.length;
       int[][] result = new int[n][n];
       
       int m1,m2,m3,m4,m5,m6,m7;
       m1 = (a[0][0] + a[1][1])*(b[0][0]+b[1][1]);
       m2 = (a[1][0] + a[1][1])*b[0][0];
       m3 = a[0][0] * (b[0][1] - b[1][1]);
       m4 = a[1][1] * (b[1][0] - b[0][0]);
       m5 =  b[1][1] *(a[0][0] + a[0][1]);
       m6 = (a[1][0] - a[0][0])*(b[0][0] + b[0][1]);
       m7 = (a[0][1] - a[1][1])*(b[1][0] + b[1][1]);
       
       result[0][0] = m1 + m4 - m5 + m7;
       result[0][1] = m3 + m5;
       result[1][0] = m2 + m4;
       result[1][1] = m1 - m2 + m3 + m6;
       
       return result;
    }
    
    
    
}


