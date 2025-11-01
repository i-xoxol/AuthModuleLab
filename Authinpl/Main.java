package main;

import com.google.gson.*;
import com.google.gson.reflect.TypeToken;

import java.io.*;
import java.lang.reflect.Type;
import java.util.ArrayList;

public class Main {
	
	public static int hashLength = 32;

	public static void main(String[] args) {
		System.out.println("Hello world!");
		
		
//		ArrayList<User> userslist = new ArrayList<User>();
//		
//		
//		
//		
//		
//		String jsonString = "{\"username\":\"user1\", \"hashedpass\":\"password\", \"salt\":\"somesalt\"}";
//		
//		GsonBuilder builder = new GsonBuilder(); 
//	    builder.setPrettyPrinting(); 
//	      
//	    Gson gson = builder.create(); 
//	    User_old user = gson.fromJson(jsonString, User_old.class); 
//	    System.out.println(user);    
//	      
//	    jsonString = gson.toJson(user); 
//	    System.out.println(jsonString);  
//	    
//	    User_old[] users = new User_old[] { new User_old("user1", "pass1", "salt1"), new User_old("user2", "pass2", "salt2"), new User_old("user3", "pass3", "salt3")};
//	    
//	    ArrayList<User_old> userlist = new ArrayList<User_old>();
//	    
//	    try (Writer writer = new FileWriter("Output.json")) {
//	        gson.toJson(users, writer);
//	    } catch (IOException e) {
//			// TODO Auto-generated catch block
//			e.printStackTrace();
//		}
//	    
//	    try {
//	    	FileReader reader = new FileReader("Output.json");
//	    	Type type = new TypeToken<ArrayList<User_old>>(){}.getType();
//	    	userlist = gson.fromJson(reader, type);
//	    }
//	    catch (IOException e) {
//			// TODO Auto-generated catch block
//			e.printStackTrace();
//		}
//	    
//	    for (User_old u: userlist) {
//	    	System.out.println(u.toString());
//	    }
		
		ArrayList<User> userslist = new ArrayList<User>();
		userslist.add(UserRegistration.createUser("user1", "password1"));
		userslist.add(UserRegistration.createUser("user2", "password2"));
		userslist.add(UserRegistration.createUser("user3", "password1"));


		
	    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	    
	    String usersFile = "usersdb.json";
	    
	    ArrayList<User> users =  AuthHelper.loadUsers(usersFile);
	    
	    if (users == null)
	    	users = new ArrayList<User>();
	    
	    AuthHelper authHelper = new AuthHelper();
	    
	        
	    while (true)
	    {
	    	
	    	System.out.println("1-login, 2-register, 3-exit:");
		    
		    String choice = null;
	    	
	    	try {
		    	choice = br.readLine();
		    }
		    catch(Exception e) {}
		    
	    	if (choice.equals("3"))
	    	{
	    		AuthHelper.saveUsers(users, usersFile);
	    		break;
	    	}
	    	
	    	if (choice.equals("2")) {
		    
	        System.out.println("Enter username: ");
	        String username=null;
			try {
				username = br.readLine();
			} catch (IOException e) {
				e.printStackTrace();
			}
			if(AuthHelper.findUser(users,  username)!=null) {
	        System.out.println("Username already Exists");
			}
			else {
				System.out.println("Enter password: ");
		        String password=null;
				try {
					password = br.readLine();
				} catch (IOException e) {
					e.printStackTrace();
				}
				users.add(UserRegistration.createUser(username, password));
				System.out.println("registration is sucessful");
			}
			}
	    	
	    	if (choice.equals("1")) {
	    		
	    		System.out.println("Enter username: ");
		        String username=null;
				try {
					username = br.readLine();
				} catch (IOException e) {
					e.printStackTrace();
				}
				
				System.out.println("Enter password: ");
		        String password=null;
				try {
					password = br.readLine();
				} catch (IOException e) {
					e.printStackTrace();
				}
				
				User userFromDB = AuthHelper.findUser(users,  username);
				if(userFromDB==null) {
					System.out.println("username or password is incorrect");
				}
				
				else {
					String salt = userFromDB.getSalt();
					String newHashedPass = authHelper.bytesToHex(authHelper.getHash(password+salt));
					if(userFromDB.getHpass ().equals(newHashedPass)) {
						System.out.println("login is correct");
					}
					else {
						System.out.println("username or password is incorrect");
					}
				}
	    		
	    	}
	        
	        
	    }
		
	   
	}

}