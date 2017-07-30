
var fso = new ActiveXObject(Scripting.FileSystemObject);
var f = fso.opentextfile("data.txt",1,true);
var obj;
obj.name = "flare";
while (!f.AtEndOfStream)
{
    f.dname = f.Readline();
    f.dnum = f.Readline();
    obj.children.f.dname = parseint(f.dnum);
}
var last = obj.toJSONString();