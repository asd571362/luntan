$(function () {

	// 注册、登录 表单切换
	$(".register-tab li").click(function () {
		$(this).addClass("active").siblings().removeClass("active");
		$(".main form").eq($(this).index()).show().siblings().hide();
	})

	// 注册表单验证
	var verify_result = false;

	function form_vf(ele,tip_ele,reg,tip_str) {	
		var input_val = ele.val();
		if (reg.test(input_val)){
			tip_ele.html("");
			return true;
		}else{
			tip_ele.html(tip_str);
			return false;
		}
		
	}

	// 1.用户名格式验证	
	var vfR_usename = false;
	var $re_usename = $("#re_usename");
	$re_usename.blur(function () {
		var $ele_tip = $('#username_tip'),
		ret = /^[a-zA-Z]\w{7,19}$/,
		tip_str = "只能包含字母、数字、'_',且必须以字母开头,长度8-20位!";
		vfR_usename = form_vf($(this),$ele_tip,ret,tip_str);
	});

	// 1.1用户名重名验证





	// alert(vfR_usename)
	// 2.密码格式验证
	var vfR_pwd = false;
	var $re_pwd = $("#re_pwd");
	$re_pwd.blur(function () {
		var $ele_tip = $('#pwd_tip'),
		ret = /^[a-zA-Z]\w{7,19}$/,
		tip_str = "只能包含字母、数字、'_',且必须以字母开头,长度8-20位!";
		vfR_pwd = form_vf($(this),$ele_tip,ret,tip_str);
	});
	// 2.密码确认
	var vfR_cpwd = false;
	var $re_cpwd = $("#re_cpwd");
	$re_cpwd.blur(function () {
		var $ele_tip = $('#cpwd_tip'),
		ret = new RegExp('^'+$re_pwd.val()+'$'),
		tip_str = "两次密码不一致！";
		vfR_cpwd = form_vf($(this),$ele_tip,ret,tip_str);
	});


	// 登录表单验证
	



})
