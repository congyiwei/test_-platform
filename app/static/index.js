// 添加项目弹出js
$(function () {
    // 添加项目弹出js
    $("#addPro").click(function () {
        $(".back").addClass('show');
    });
    $(".closeImage").click(function () {
        $(".back").removeClass('show');
    });
    $(".SubmissionPro").click(function () {
        $(".back").removeClass('show');
    });
    //侧边栏
    $(".left_menu_li h3").click(function () {
        //代表当前节点
        //toggleClass该方法检查每个元素中指定的类。如果不存在则添加类，如果已设置则删除之。这就是所谓的切换效果。
        // $(this).siblings().toggleClass("show");
        // $(this).parent().siblings().children("ul").removeClass("show");
         $(this).siblings().toggle();
         $(this).parent().siblings().children("ul").hide();
        // $(this).siblings().slideToggle();
        // $(this).parent().siblings().children("ul").slideUp();
    })
});

