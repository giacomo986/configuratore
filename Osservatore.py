class SelObserver:
	def setPreselection(self,doc,obj,sub):                # Preselection object
		#App.Console.PrintMessage(str(sub)+ " puzza 1\n")          # The part of the object name
		pass

	def addSelection(self,doc,obj,sub,pnt):               # Selection object
		#App.Console.PrintMessage("addSelection"+ "\n")
		#App.Console.PrintMessage(str(doc)+ "\n")          # Name of the document
		#App.Console.PrintMessage(str(obj)+ "\n")          # Name of the object
		#App.Console.PrintMessage(str(sub)+ "\n")          # The part of the object name
		#App.Console.PrintMessage(str(pnt)+ "\n")          # Coordinates of the object
		#App.Console.PrintMessage("______"+ "\n")
		if (str(obj)[:13] == "Inizio_nastro"):
			FreeCAD.Console.PrintMessage("cliccato su sfera " + str(obj) + "\n")
		if (str(obj)[:11] == "Fine_nastro"):
			FreeCAD.Console.PrintMessage("cliccato su sfera " + str(obj) + "\n")

			#RichiestaNastroCurva()

		if (str(obj)[:15] == "Fianco_sinistro"):
			FreeCAD.Console.PrintMessage("cliccato su " + str(obj) + "\n")
		if (str(obj)[:13] == "Fianco_destro"):
			FreeCAD.Console.PrintMessage("cliccato su " + str(obj) + "\n")

	def removeSelection(self,doc,obj,sub):                # Delete the selected object
		#App.Console.PrintMessage("removeSelection"+ " puzza 8\n")
		pass
	
	def setSelection(self,doc):                           # Selection in ComboView
		#App.Console.PrintMessage("setSelection"+ " puzza 9\n")
		pass
	
	def clearSelection(self,doc):                         # If click on the screen, clear the selection
		#App.Console.PrintMessage("clearSelection"+ " puzza 10\n")  # If click on another object, clear the previous object
		pass

