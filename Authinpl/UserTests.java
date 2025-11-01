package main;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class UserTests {

	@Test
	void toStringTest() {
		
		User user = new User("user1", "password", "salt");
		String output = "User: user1, password, salt";
		if(!user.toString().equals(output))
			fail("User is not created properly");
	}
	
	@Test
	void equalsTest() {
		User user1 = new User("user1", "password", "salt");
		User user2 = new User("user2", "password", "salt");
		User user3 = new User("user1", "password", "salt");
		
		if (user1.equals(user2))
			fail("different users are equal");
		
		if (!user1.equals(user3))
			fail("same usernames are not equal");
		
	}
	@Test
	void saveLoadUsersTest() {

		ArrayList<User> usersToSave = new ArrayList<User>();
		usersToSave.add(UserRegistration.createUser("User1", "password"));
		usersToSave.add(UserRegistration.createUser("User2", "password"));
		usersToSave.add(UserRegistration.createUser("User3", "password"));
	
		String userFile = "users.json";
	
		AuthHelper.saveUsers(usersToSave, UserFile);
	
		ArrayList<User> loadedUsers = AuthHelper.loadUsers(userFile);
	
		if (loadedUsers==null || loadedUsers.size()==0)
		fail("Users were not loaded")
		
		for (int i=0; i<usersToSave.size(); i++) {
			if(!usersToSave.get(i).getUsername(). equals(loadedUsers.get(i).getUsername()))
				fail("user name is wrong");
			
			if(!usersToSave.get(i).getHpass(). equals(loadedUsers.get(i).getHpass()))
				fail("user name is wrong");
					
			if(!usersToSave.get(i).getSalt(). equals(loadedUsers.get(i).getSalt()))
				fail("user name is wrong");
			
		}
@test
void findTest() {
		ArrayList<User> usersToSave = new ArrayList<User>();
		usersToSave.add(UserRegistration.createUser("User1", "password"));
		usersToSave.add(UserRegistration.createUser("User2", "password"));
		usersToSave.add(UserRegistration.createUser("User3", "password"));
	
		String userFile = "users.json";
	
		AuthHelper.saveUsers(usersToSave, UserFile);
	
		ArrayList<User> loadedUsers = AuthHelper.loadUsers(userFile);
	
		if (loadedUsers==null || loadedUsers.size()==0)
		fail("Users were not loaded")
		
		for (int i=0; i<usersToSave.size(); i++) {
			if(!usersToSave.get(i).getUsername(). equals(loadedUsers.get(i).getUsername()))
				fail("user name is wrong");
			
			if(!usersToSave.get(i).getHpass(). equals(loadedUsers.get(i).getHpass()))
				fail("user name is wrong");
					
			if(!usersToSave.get(i).getSalt(). equals(loadedUsers.get(i).getSalt()))
				fail("user name is wrong");
		}
		@test 
	}
}

