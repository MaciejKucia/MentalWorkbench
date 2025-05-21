```ada
--  AVR Studio 5 Device definition XML to ADA processor
--  Krakow 2012
--
--  Copyright (C) 2012 Maciej Kucia
--  
--  Permission is hereby granted, free of charge, to any person obtaining a copy
--  of this software and associated documentation files (the "Software"), 
--  to deal in the Software without restriction, including without limitation 
--  the rights to use, copy, modify, merge, publish, distribute, sublicense, 
--  and/or sell copies of the Software, and to permit persons to whom the 
--  Software is furnished to do so, subject to the following conditions:
--  
--  The above copyright notice and this permission notice shall be included in 
--  all copies or substantial portions of the Software.
--  
--  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
--  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
--  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
--  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
--  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM
--  , OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN 
--  THE SOFTWARE.


with Input_Sources.File; use Input_Sources.File;
with Sax.Readers;        use Sax.Readers;
with DOM.Readers;        use DOM.Readers;
with DOM.Core;           use DOM.Core;
with DOM.Core.Documents; use DOM.Core.Documents;
with DOM.Core.Nodes;     use DOM.Core.Nodes;
with DOM.Core.Attrs;     use DOM.Core.Attrs;
with Ada.Text_IO;        use Ada.Text_IO;
with Ada.Strings.Fixed;	 use Ada.Strings.Fixed;
with Ada.Command_Line;	 use Ada.Command_Line;
with Ada.Exceptions;	 use Ada.Exceptions;

procedure Main is
   Input  : File_Input;
   List   : Node_List; 
   List2  : Node_List;
   List3  : Node_List;
   Reader : Tree_Reader;
   Doc    : Document;
   N      : Node;
   A      : Attr;
   AA     : Attr;
   AAA    : Attr;
   B      : Attr;
   C      : Attr;
begin
   
   if Ada.Command_Line.Argument_Count /= 1 then
      Put_Line("Usage: main <DEVICE>.xml > AVR-<DEVICE>.ads");
      Put_Line("Where <DEVICE> is device name ex. AtMega8.xml");
      return;
   end if;
   
   
   Open (Ada.Command_Line.Argument(1), Input);
   Set_Feature (Reader, Validation_Feature, False);
   Set_Feature (Reader, Namespace_Feature, False);
   Parse (Reader, Input);
   Close (Input);

   Doc := Get_Tree (Reader);
   
   
   Put_Line("with Interfaces; use Interfaces;");
   Put_Line("with System;");   

   List := Get_Elements_By_Tag_Name(Doc, "device");
   AAA := Get_Named_Item(Attributes(Item(List,0)), "name");
   
   A := Get_Named_Item(Attributes(Item(List,0)), "architecture");
   Put_Line("");
   Put_Line("  -- architecture = "& Value(A));
   Put_Line("  -- AVR Studio 5 XML avr register definition generator ");
   Put_Line("  -- Maciej Kucia, Krakow 2012 ");
   Put_Line("");
   

   Put_Line("package AVR."& Value(AAA) & " is");
   
   List := Get_Elements_By_Tag_Name (Doc, "register-group");
   for Index in 1 .. Length (List) loop 
      N := Item (List, Index - 1);
      A := Get_Named_Item (Attributes (N), "name");

      List2 := Child_Nodes(N);
      
      for Index2 in 1 .. Length (List2) loop
         N := Item (List2, Index2 - 1);
         
         if (Name(N) = "register") then 
            B := Get_Named_Item (Attributes (N), "caption");
            if Value(B) /= "" then 

               Put_Line("");
               Put_Line("  --");
               Put_Line("  --  " & Value (A));
               Put_Line("  --");
               Put_Line("");
               
               Put_Line("  -- " & Value(B));
               A := Get_Named_Item (Attributes (N), "name");
               Put_Line("  " & Value(A) & " : Unsigned_8;");
               C := Get_Named_Item (Attributes (N), "offset");
               Put_Line("  for " & Value(A) & "'Address" & ASCII.HT & 
                        " use System'To_Address (16#" & Tail(Value(C),2) & "#);");
               Put_Line("");
            
               List3 := Child_Nodes(N);
            
               for Index3 in 1 .. Length (List3) loop
                  N := Item (List3, Index3 - 1);
         
                  if (Name(N) = "bitfield") then 
                     B  := Get_Named_Item (Attributes (N), "caption");
                     AA := Get_Named_Item (Attributes (N), "name");
                     C  := Get_Named_Item (Attributes (N), "mask");
                     Put_Line("   " & Value(A) & "_" & Value(AA) & ASCII.HT & ASCII.HT 
                              & ": constant := 16#" & Tail(Value(C),2) & "#; -- " & Value(B));
                  end if;
               
               end loop;
            
               Put_Line("");
            end if;
         end if;
      end loop;
      
   end loop; 
   
   Put_Line("end AVR."& Value(AAA) & ";");
  
   Free (List);
   Free (Reader);
   
exception
   when e: Others =>
      Put_Line("ERROR:");
      Put_Line(Ada.Exceptions.Exception_Message(e));
      Put_Line(Ada.Exceptions.Exception_Information(e));
end Main;
```