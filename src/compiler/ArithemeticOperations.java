/**
 * 
 */
package compiler;

import java.util.List;

/**
 * @author pankajsingh
 *
 */
public class ArithemeticOperations {

	int a,b;
	boolean x,y;
	String resV="TOP";
	String resB="TOPB";
	private void extractAB(Statement smt) {
		// TODO Auto-generated method stub
		String op1=smt.getOp1();
		String op2=smt.getOp2();
		 a=ReservedKeywords.getINTValue(op1);
		 b=ReservedKeywords.getINTValue(op2);
		
	}
	private void extractXY(Statement smt) {
		// TODO Auto-generated method stub
		String op1=smt.getOp1();
		String op2=smt.getOp2();
		 x=ReservedKeywords.getBoolValue(op1);
		 y=ReservedKeywords.getBoolValue(op2);
		
	}
	public void executeADD(Statement smt) {
		// TODO Auto-generated method stub
		extractAB(smt);
		int res=a+b;
		ReservedKeywords.setTop(res);
		//ReservedKeywords.setINT(resV, res);
	}
	public void executeSUB(Statement smt) {
		// TODO Auto-generated method stub
		extractAB(smt);
		int res=a-b;
		ReservedKeywords.setTop(res);
		//ReservedKeywords.setINT(resV, res);
	}
	public void executeMUL(Statement smt) {
		// TODO Auto-generated method stub
		extractAB(smt);
		int res=a*b;
		ReservedKeywords.setTop(res);
		//ReservedKeywords.setINT(resV, res);
	}
	public void executeDIV(Statement smt) {
		// TODO Auto-generated method stub
		extractAB(smt);
		int res=a/b;
		ReservedKeywords.setTop(res);
		//ReservedKeywords.setINT(resV, res);
	}
	public void executeMOD(Statement smt) {
		// TODO Auto-generated method stub
		extractAB(smt);
		int res=a%b;
		ReservedKeywords.setTop(res);
		//ReservedKeywords.setINT(resV, res);
	}
	public void executeAND(Statement smt) {
		// TODO Auto-generated method stub
		extractXY(smt);
		boolean res=x&&y;
		//ReservedKeywords.setBool(resB, res);
		ReservedKeywords.setTopb(res);
		
		
	}
	public void executeOR(Statement smt) {
		// TODO Auto-generated method stub
		extractXY(smt);
		boolean res=x||y;
		//ReservedKeywords.setBool(resB, res);
		ReservedKeywords.setTopb(res);
		
	}
	//comparison operations
	public void executeSML(Statement smt) {
		// TODO Auto-generated method stub
		extractAB(smt);
		boolean res=a<b;
		//ReservedKeywords.setBool(resB, res);
		ReservedKeywords.setTopb(res);
	}
	public void executeSMLEQL(Statement smt) {
		// TODO Auto-generated method stub
		extractAB(smt);
		boolean res=a<=b;
		//ReservedKeywords.setBool(resB, res);
		ReservedKeywords.setTopb(res);
	}
	public void executeGRT(Statement smt) {
		// TODO Auto-generated method stub
		extractAB(smt);
		boolean res=a>b;
		//ReservedKeywords.setBool(resB, res);
		ReservedKeywords.setTopb(res);
	}
	public void executeGRTEQL(Statement smt) {
		// TODO Auto-generated method stub
		extractAB(smt);
		boolean res=(a>=b);
		//ReservedKeywords.setBool(resB, res);
		ReservedKeywords.setTopb(res);
	}
	public void executeEQL(Statement smt) {
		// TODO Auto-generated method stub
		extractAB(smt);
		boolean res=(a==b);
		//ReservedKeywords.setBool(resB, res);
		ReservedKeywords.setTopb(res);
	}
	public void executeNOTEQL(Statement smt) {
		// TODO Auto-generated method stub
		extractAB(smt);
		boolean res=(a!=b);
		//ReservedKeywords.setBool(resB, res);
		ReservedKeywords.setTopb(res);
	}
	public int executeGOTO(List<String> statements, Statement smt) throws Exception {
		// TODO Auto-generated method stub
		String var=smt.getOp1();
		int index=ReservedKeywords.getINTValue(var);
		String branch=statements.get(index);
		Statement branchedStatement=new Statement();
		branchedStatement.createStatement(branch);
		String operation=branchedStatement.getOperation();
		if("IF".equals(operation)||"ELSE".equals(operation)||"LOOP".equals(operation)||"END".equals(operation))
			return index;
		else 
			throw new Exception("Branching to unknown destination");
		
	}	

}
