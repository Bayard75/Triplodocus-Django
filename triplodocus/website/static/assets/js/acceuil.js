function truncateString(str, num) {
    if (num >= str.length)
    {
        return str.substring(0,num);

    }
    return str.substring(0,num) + "...";
  }
  
  console.log(truncateString("A-tisket a-tasket A green and yellow basket", "A-tisket a-tasket A green and yellow basket".length));
  