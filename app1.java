// filename: VulnerableApp.java

import java.sql.*;
import java.util.Scanner;

public class VulnerableApp {

    // 하드코딩된 API 키 (Secrets 탐지용)
    private static final String API_KEY = "abcd1234-this-is-insecure";

    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter username: ");
        String username = scanner.nextLine();

        System.out.print("Enter password: ");
        String password = scanner.nextLine();

        // SQL Injection 취약점 포함된 쿼리
        String query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'";

        Connection conn = DriverManager.getConnection("jdbc:sqlite:users.db");
        Statement stmt = conn.createStatement();
        ResultSet rs = stmt.executeQuery(query);

        if (rs.next()) {
            System.out.println("Login success");
        } else {
            System.out.println("Login failed");
        }

        rs.close();
        stmt.close();
        conn.close();
    }
}
