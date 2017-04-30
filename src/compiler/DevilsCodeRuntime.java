/**
 * 
 */
package compiler;

import java.util.ArrayList;
import java.util.List;

/**
 * @author pankajsingh
 * @Date : April 14, 2017
 * @version: 5
 * @Purpose: Main class and starting class for the Devilscode runtime
 * 
 *
 */
public class DevilsCodeRuntime {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		DevilsCodeRuntime coder=new DevilsCodeRuntime();
		List<String> statements= null;
		if(1>args.length)
			statements=coder.readFile();
		else
		{
			//System.out.println(args[0]);
			statements=coder.readFile(args[0]);
		}
//		for(String s: statements)
//		{
//			System.out.println(s);
//		}
		ReservedKeywords.init();
		StatementsExecutor executor=new StatementsExecutor(statements);
		List<String> output=executor.generateOutput();
		for(String o:output)
		{
			System.out.println(o);
		}
		

	}
	public List<String> readFile()
	{
		//write file name logic if required
		StatementsReader reader=new StatementsReader();
		return reader.readFile();
	}
	public List<String> readFile(String file)
	{
		//write file name logic if required
		
		StatementsReader reader=new StatementsReader();
		return reader.readFile(file);
	}

}
