$(function () {

	// 注册、登录 表单切换
	$(".register-tab li").click(function () {
		$(this).addClass("active").siblings().removeClass("active");
		$(".main form").eq($(this).index()).show().siblings().hide();
	})

	// 注册表单验证
	var re_name_bl = "";
	// 1.1用户名重名验证
	function re_ajax() {
		var post_name = {'post_name':$re_usename.val()};
		$.ajax({
			'url':'uname_re_vf/',
			'type':'post',
			'async':false,
			'data':post_name,
			'dataType':'json'
		}).done(function (dat) {
			if(dat.nlength){
				$username_tip.html("该用户名已存在！");
				re_name_bl = false;
			}else {
				re_name_bl = true;
			}

		}).fail(function () {
			$username_tip.html("连接服务器失败！");
		})
    }

	// 1.用户名格式验证
	var $re_usename = $("#re_usename");
	var $username_tip = $('#username_tip');
	var ret_usename= /^[a-zA-Z]\w{7,19}$/;
	var usename_str = "只能包含字母、数字、'_',且必须以字母开头,长度8-20位!";
	$re_usename.blur(function () {
		var input_val = $(this).val();

		if (ret_usename.test(input_val)){
			$username_tip.html("")
			// 1.1用户名重名验证
			re_ajax();
		}else {
            $username_tip.html(usename_str);
        }
	})

	// 2.密码格式验证
	var $re_pwd = $("#re_pwd");
	var $pwd_tip = $('#pwd_tip');
	var ret_pwd= /^[a-zA-Z]\w{5,19}$/;
	var pwd_str = "只能包含字母、数字、'_',且必须以字母开头,长度6-20位!";
	$re_pwd.blur(function () {
		var input_val = $(this).val();
		if (ret_pwd.test(input_val)){
			$pwd_tip.html("")
		}else{
			$pwd_tip.html(pwd_str);
		}
	})



	// 2.密码确认
	var $re_cpwd = $("#re_cpwd");
	var $cpwd_tip = $('#cpwd_tip');
	var cpwd_str = "两次密码不一致!";
	$re_cpwd.blur(function () {
		if ($re_pwd.val() == $(this).val()){
			$cpwd_tip.html("")
		}else{
			$cpwd_tip.html(cpwd_str);
		}
	});

	// 提交验证
	$('#reg_submit').click(function () {

		re_ajax();

		var vf_register = re_name_bl && ret_usename.test($re_usename.val()) && ret_pwd.test($re_pwd.val()) && ($re_pwd.val() == $re_cpwd.val());

		if (vf_register == false){
			alert("信息输入有误,请重新输入！");
		}else {
			$('.register-form').submit();
		}
	})



	// 登录表单验证
	var log_vf = false;
	function log_ajax() {
		var post_info = {
			'post_name':$login_usename.val(),
			'post_pwd':$login_pwd.val(),
			'post_type':'ajax',
						};

		$.ajax({
			'url':'login_post/',
			'async':false,
			'type':'post',
			'data':post_info,
			'dataType':'json'
		}).done(function (dat) {
			if(dat.log_vf == false){
				$('#login_tip').html("用户名或密码错误")
			}else {
				log_vf = true;
				$('#login_tip').html("")
			}

		}).fail(function () {
			$username_tip.html("连接服务器失败！");
		})
    }

    var $login_usename = $('#login_usename'),
		$login_pwd = $('#login_pwd');

	$('#log_submit').click(function () {
		log_ajax();
		if (log_vf){
			alert("登陆成功！");
			window.location.href = '/index';
		}
	})



})
