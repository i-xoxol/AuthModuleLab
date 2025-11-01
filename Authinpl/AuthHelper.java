package main;

import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;
import java.util.ArrayList;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.reflect.TypeToken;

import java.io.*;
import java.lang.reflect.Type;

public class AuthHelper {
	
	public byte[] getSalt(int length) {
		byte[] result = new byte[length];
		
		SecureRandom random = new SecureRandom();
		random.nextBytes(result);
		
		return result;
	}
	
	public byte[] getHash(String input) {
		byte[] result = null;
		try {
			MessageDigest digest = MessageDigest.getInstance("SHA-256");
			result = digest.digest(
					input.getBytes(StandardCharsets.UTF_8));
		} catch (NoSuchAlgorithmException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} 
		
		return result;
	}
	
	public static String bytesToHex(byte[] hash) {
	    StringBuilder hexString = new StringBuilder(2 * hash.length);
	    for (int i = 0; i < hash.length; i++) {
	        String hex = Integer.toHexString(0xff & hash[i]);
	        if(hex.length() == 1) {
	            hexString.append('0');
	        }
	        hexString.append(hex);
	    }
	    return hexString.toString();
	}
	
	public static User jsonToUser(String json) {
		User user = null;
		
		GsonBuilder builder = new GsonBuilder(); 
	    builder.setPrettyPrinting(); 
	      
	    Gson gson = builder.create(); 
	    user = gson.fromJson(json, User.class);
		
		return user;
	}
	
	public static String userToJson(User user) {
		String jsonString = null;
		
		GsonBuilder builder = new GsonBuilder(); 
	    builder.setPrettyPrinting(); 
	      
	    Gson gson = builder.create(); 
		jsonString = gson.toJson(user);
		
		return jsonString;
	}
	
	public static User findUser(ArrayList<User> userlist, String username) {
		User user = null;
		
		for (User u : userlist) {
			if (u.getUsername().equalsIgnoreCase(username))
				return u;
		}
		
		return user;
	}
	
	public static void saveUsers(ArrayList<User> userslist, String filepath) {
		
		GsonBuilder builder = new GsonBuilder(); 
	    builder.setPrettyPrinting(); 
	      
	    Gson gson = builder.create();
		
		try (Writer writer = new FileWriter(filepath)) {
	        gson.toJson(userslist, writer);
	    } catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	public static ArrayList<User> loadUsers(String filepath){
		ArrayList<User> userslist = null;
		
		GsonBuilder builder = new GsonBuilder(); 
	    builder.setPrettyPrinting(); 
	      
	    Gson gson = builder.create();
		
		try {
	    	FileReader reader = new FileReader(filepath);
	    	Type type = new TypeToken<ArrayList<User>>(){}.getType();
	    	userslist = gson.fromJson(reader, type);
	    }
	    catch (IOException e) {
			e.printStackTrace();
	    }
		
		return userslist;
	}

}
