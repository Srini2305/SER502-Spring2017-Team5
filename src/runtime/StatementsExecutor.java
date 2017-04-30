/**
 * 
 */
package runtime;

import java.util.ArrayList;
import java.util.List;

/**
 * @author pankajsingh
 * @Date : April 14, 2017
 * @version: 9
 * @Purpose: For identification and execution of statements 
 * 
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
		boolean gotoSkipped=false;
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
							gotoSkipped=skipGOTO(branching);
							break;
				case "EQL": ariOps.executeEQL(smt);
							gotoSkipped=skipGOTO(branching);
							break;	
				case "GTR": ariOps.executeGRT(smt);
							gotoSkipped=skipGOTO(branching);
							break;	
				case "SMLEQL": ariOps.executeSMLEQL(smt);
							gotoSkipped=skipGOTO(branching);
							break;		
				case "GRTEQL": ariOps.executeGRTEQL(smt);
							gotoSkipped=skipGOTO(branching);
							break;	
				case "NOTEQL": ariOps.executeNOTEQL(smt);
							gotoSkipped=skipGOTO(branching);
							break;
				//branching statements
				case "IF" :	branching =true;
							break;
				case "ELSE" :	if(branching&&!gotoSkipped)
								index++;//skip GOTO statement
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
	private boolean skipGOTO(boolean branching)
	{
		String stat=statements.get(index+1);
		boolean val=stat.contains("GOTO");
		if(val&&branching&&ReservedKeywords.getTopb())
		{
			index++;//skip GOTO statement
			return true;
		}
		return false;
	}
	

}
