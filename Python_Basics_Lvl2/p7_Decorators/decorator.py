def new_decorator(func):

  def wrap_func():
    print("Code before executing func")
    func()
    print("Func() has been called")
  
  return wrap_func()

@new_decorator
def func_needs_decorator():
  print("This function is in need to decorator")


#func_needs_decorator = new_decorator(func_needs_decorator)
func_needs_decorator();