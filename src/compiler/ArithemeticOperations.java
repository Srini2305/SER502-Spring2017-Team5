/**
 * 
 */
package compiler;

/**
 * @author pankajsingh
 *
 */
public class ArithemeticOperations {

	int a,b;
	String resV="TOP";
	private void extractAB(Statement smt) {
		// TODO Auto-generated method stub
		String op1=smt.getOp1();
		String op2=smt.getOp2();
		 a=ReservedKeywords.getINT(op1);
		 b=ReservedKeywords.getINT(op2);
		
	}
	public void executeADD(Statement smt) {
		// TODO Auto-generated method stub
		extractAB(smt);
		int res=a+b;
		ReservedKeywords.setINT(resV, res);
	}
	public void executeSUB(Statement smt) {
		// TODO Auto-generated method stub
		extractAB(smt);
		int res=a-b;
		ReservedKeywords.setINT(resV, res);
	}
	public void executeMUL(Statement smt) {
		// TODO Auto-generated method stub
		extractAB(smt);
		int res=a*b;
		ReservedKeywords.setINT(resV, res);
	}
	public void executeDIV(Statement smt) {
		// TODO Auto-generated method stub
		extractAB(smt);
		int res=a/b;
		ReservedKeywords.setINT(resV, res);
	}
	public void executeMOD(Statement smt) {
		// TODO Auto-generated method stub
		extractAB(smt);
		int res=a/b;
		ReservedKeywords.setINT(resV, res);
	}
	

}
