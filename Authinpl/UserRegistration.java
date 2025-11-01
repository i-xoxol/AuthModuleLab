package main;

public class UserRegistration {
	
	public static User createUser(String username, String password) {
		User user=null;
		
		AuthHelper helper = new AuthHelper();
		String salt = helper.bytesToHex(helper.getSalt(32));
		String passsalt = password+salt;
		String hashedpass = helper.bytesToHex(helper.getHash(passsalt));
		
		user = new User(username, hashedpass, salt);
		
		return user;
	}

}
