# Shell script file rw and displaying

echo "Enter filename: ";read name;
echo "Enter Starting Line (No.): "; read fline;
echo "Enter Ending Line: "; read lline;

sed -n "$fline,$lline p" $name > newline
cat newline

