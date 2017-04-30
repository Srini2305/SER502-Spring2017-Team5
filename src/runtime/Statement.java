package runtime;

import java.util.HashSet;
import java.util.Set;

import javax.swing.text.html.HTMLDocument.HTMLReader.IsindexAction;
/**
 * @author pankajsingh
 * @Date : April 14, 2017
 * @version: 2
 * @Purpose: For Statement breakup  
 * 
 *
 */
public class Statement {
	
	private int lineNo;
	private String operation;
	private String op1;
	private String op2;
	
	public void createStatement(String smt) throws Exception {
		
		String[] tokens=smt.split(" ");
		this.lineNo = Integer.parseInt(tokens[0]);
		if(null!=tokens[1]&&ReservedKeywords.isOperation(tokens[1]))
		{
			this.operation = tokens[1].trim();
		}
		else{
			throw new Exception("Operation not found");
		}
		
		if(tokens.length>2)
				this.op1 = tokens[2].trim();
		if(tokens.length>3)
			this.op2 = tokens[3].trim();
		
	}
	public int getLineNo() {
		return lineNo;
	}
	public void setLineNo(int lineNo) {
		this.lineNo = lineNo;
	}
	public String getOperation() {
		return operation;
	}
	public void setOperation(String operation) {
		this.operation = operation;
	}
	public String getOp1() {
		return op1;
	}
	public void setOp1(String op1) {
		this.op1 = op1;
	}
	public String getOp2() {
		return op2;
	}
	public void setOp2(String op2) {
		this.op2 = op2;
	}
	

}
