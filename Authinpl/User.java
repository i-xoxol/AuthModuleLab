package main;

public class User {
	
	private String username, hpass, salt;
	
	

	public User(String username, String hpass, String salt) {
		super();
		this.username = username;
		this.hpass = hpass;
		this.salt = salt;
	}

	public String getUsername() {
		return username;
	}

	public void setUsername(String username) {
		this.username = username;
	}

	public String getHpass() {
		return hpass;
	}

	public void setHpass(String hpass) {
		this.hpass = hpass;
	}

	public String getSalt() {
		return salt;
	}

	public void setSalt(String salt) {
		this.salt = salt;
	}

	@Override
	public boolean equals(Object obj) {
		
		if (this==obj)
			return true;
		
		if (!(obj instanceof User))
			return false;
		
		User u = (User)obj;		
		
		return username.equalsIgnoreCase(u.getUsername());
	}

	@Override
	public String toString() {
		
		return "User: " + username + ", " + hpass + ", " + salt;
	}
	
	
	

}
