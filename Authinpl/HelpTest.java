package main;

import static org.junit.Assert.*;

import org.junit.Test;

public class HelpTest {

	@Test
	public void testGetSalt() {
		//fail("Not yet implemented");
		
		byte[] testResult1 = null;
		byte[] testResult2 = null;

		AuthHelper utils = new AuthHelper();
		
		testResult1 = utils.getSalt(Main.hashLength);
		
		if (testResult1==null)
			fail("Salt is NULL");
		
		if (testResult1.length != Main.hashLength)
			fail("Salt length is incorrect");
		
		testResult2 = utils.getSalt(Main.hashLength);
		
		if (testResult1.equals(testResult2)) {
			fail("Randomness does not work!");
		}
		
	}
	
	@Test
	public void testGetHash() {
		String testString = "TEST";
		String testHash = "94ee059335e587e501cc4bf90613e0814f00a7b08bc7c648fd865a2af6a22cc2";
		AuthHelper utils = new AuthHelper();
		byte[] hashResult = utils.getHash(testString);
		
		if (hashResult == null)
			fail("Hash result is NULL");
		
		if(!testHash.equals(utils.bytesToHex(hashResult)))
				fail("Hash is wrong!");
	}
	
	@Test
	public void testJsonToUser() {
		String json = "{\"username\":\"user1\", \"hpass\":\"password\", \"salt\":\"somesalt\"}";
		User user = new User("user1", "password", "somesalt");
		
		User userFromJson = AuthHelper.jsonToUser(json);
		
		System.out.println(userFromJson.toString());
		
		if(!user.equals(userFromJson))
			fail("Json to User failed");

	}

}
