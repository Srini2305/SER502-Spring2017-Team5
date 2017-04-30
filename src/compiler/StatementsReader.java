/**
 * 
 */
package compiler;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * @author pankajsingh
 * @Date : April 14, 2017
 * @version: 2
 * @Purpose: For reading intermediate code file  
 * 
 *
 */
public class StatementsReader {
	String pathName="./intermediateCode/";
	String fileName="NestedIf.txt";
	public String getPathName() {
		return pathName;
	}
	public void setPathName(String pathName) {
		this.pathName = pathName;
	}
	public String getFileName() {
		return fileName;
	}
	public void setFileName(String fileName) {
		this.fileName = fileName;
	}
	public List<String> readFile()
	{
		
		return readFile(pathName+fileName);
		
	}
	public List<String> readFile(String fileName)
	{
		List<String> lines=new ArrayList<String>();
		
		try(BufferedReader br = new BufferedReader(new FileReader(fileName))) {
			String line = br.readLine();
			while(line!=null){
		    lines.add(line);
		    line= br.readLine();
		    }
		    
		    
		}
		
		catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return lines;
	}
	

}
