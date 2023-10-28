import org.apache.commons.dbcp2.BasicDataSource;

import java.sql.Connection;
import java.sql.SQLException;

public class DatabaseConnectionExample {
    public static void main(String[] args) {
        // Create a DataSource (connection pool)
        BasicDataSource dataSource = new BasicDataSource();
        dataSource.setDriverClassName("com.mysql.cj.jdbc.Driver");
        dataSource.setUrl("jdbc:mysql://localhost:3306/your_database_name");
        dataSource.setUsername("your_username");
        dataSource.setPassword("your_password");

        // Get a connection from the pool
        try (Connection connection = dataSource.getConnection()) {
            // Use the connection to execute SQL queries
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
