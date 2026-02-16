def conver_seconds(total_seconds: int) -> str;
  minutes = total_seconds // 60
  seconds = total_seconds % 60
  return f"\"{minutes}m {seconds}s\""
total_seconds = int(input("Enter total seconds:"))
print(convert_seconds(total_seconds))