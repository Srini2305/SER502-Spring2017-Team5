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
public class StatementsExecutor {
	List<String> statements;
	DeclarativeOperations dec;
	ArithemeticOperations ariOps;
	int index;
	public StatementsExecutor(List<String> statements)
	{
		this.statements=statements;
		dec=new DeclarativeOperations();
		ariOps=new ArithemeticOperations();
		
	}
	public List<String> generateOutput()
	{
		List<String> output=new ArrayList<String>();
		int len=statements.size();
		Statement smt=new Statement();
		boolean branching=false;
		for( index=0;index<len;index++)
		{
			try {
				smt.createStatement(statements.get(index));
			
			switch(smt.getOperation())
			{
			//declarative statements
				case "START": dec.executeStart(smt);
								break;
				case "STOP": dec.executeStop(smt,len);
								break;	
				case "BEGIN": dec.executeBegin(smt);
								break;
				case "END": dec.executeEnd(smt);
								break;	
				case "PRINT": String value=dec.executePrint(smt);
								output.add(value);
								break;	
				case "DEC": dec.executeDec(smt);
								break;
				case "ASSN": dec.assignValue(smt);
								break;	
								
								
			//Arithmetic Statements	
								
				case "ADD": ariOps.executeADD(smt);
							break;	
				case "SUB": ariOps.executeSUB(smt);
							break;	
				case "MUL": ariOps.executeMUL(smt);
							break;	
				case "DIV": ariOps.executeDIV(smt);
							break;
				case "MOD": ariOps.executeMOD(smt);
							break;	
				//boolean operations
				case "AND": ariOps.executeAND(smt);
							break;
				case "OR": ariOps.executeOR(smt);
							break;				
				//boolean operations
				case "SML": ariOps.executeSML(smt);
							skipGOTO(branching);
							break;
				case "EQL": ariOps.executeEQL(smt);
							skipGOTO(branching);
							break;	
				case "GRT": ariOps.executeGRT(smt);
							skipGOTO(branching);
							break;	
				case "SMLEQL": ariOps.executeSMLEQL(smt);
							skipGOTO(branching);
							break;		
				case "GRTEQL": ariOps.executeGRTEQL(smt);
							skipGOTO(branching);
							break;	
				case "NOTEQL": ariOps.executeNOTEQL(smt);
							skipGOTO(branching);
							break;
				//branching statements
				case "IF" :	branching =true;
							break;
				case "LOOP" :branching =true;
							break;	
				case "GOTO" ://implement GOTO
							int i=ariOps.executeGOTO(statements,smt);
							index=i-1;
							//branching =true;
							break;				
							
			}

			} catch (Exception e) {
				// TODO Auto-generated catch block
				output.add("Error: "+e.getMessage()+" :: line: "+smt.getLineNo());
				return output;
			}
		}
		return output;
	}
	private void skipGOTO(boolean branching)
	{
		if(branching&&ReservedKeywords.getBool(ReservedKeywords.topb))
			index++;//skip GOTO statement
	}
	

}
