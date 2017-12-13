$(function () {
    var time1 = setInterval(function () {
        var dateFull = new Date(),
            year = dateFull.getFullYear(),
            month = dateFull.getMonth()+1,
            day = dateFull.getDate(),
            hour = dateFull.getHours(),
            minute = dateFull.getMinutes(),
            second = dateFull.getSeconds();
        console.log(dateFull);
        var date_str = year + "年"+ month + "月"+ day +"日";
        var time_str = hour + "时"+ minute + "分"+ second +"秒";


        $('.time-date').html(date_str)
        $('.time-time').html(time_str)

    },500)
})