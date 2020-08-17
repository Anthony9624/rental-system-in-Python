/*判断字符串是否为空*/
function isEmpty(obj){
    if(typeof obj == "undefined" || obj == null || obj == ""){
        return true;
    }else{
        return false;
    }
}

/*检查输入框是否为空*/
function submitLogin() {
    var user_val = userloginform.username.value;
    var password_val = userloginform.password.value;
    var verify_val = userloginform.verifycode.value;
    if (isEmpty(user_val))
    {
        alert("当前用户名未填!");
        return false;
    }
    if (isEmpty(password_val))
    {
        alert("当前密码未填!");
        return false;
    }
    if (isEmpty(verify_val))
    {
        alert("当前验证码未填!");
        return false;
    }
    return true; //默认不提交
}


/*接收后端传来的数据、用来响应显示密码错误*/
/*
* var List =  {%errorinfo };
if(!List.empty())
{
    alert(List);
}
* */