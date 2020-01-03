i = 1;
while(i<10)
{
    document.write("<h2>"+i+"</h2>");
    i += 1;
    if(i==8)
    {
        document.write("Time to break up");
        break;
    }
}