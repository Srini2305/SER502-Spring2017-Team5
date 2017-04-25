/**
 * 
 */
package compiler;

import java.util.ArrayList;
import java.util.List;

/**
 * @author pankajsingh
 *
 */
public class DevilsCodeRuntime {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		DevilsCodeRuntime coder=new DevilsCodeRuntime();
		List<String> statements= coder.readFile();
		for(String s: statements)
		{
			System.out.println(s);
		}
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

}
