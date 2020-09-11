function form_on_submit(url_path, table_id) {
    layui.form.on('submit(save)', function (data) {
        layui.jquery.ajax({
            type: "POST",
            url: url_path,
            data: data.field,
            dataType: "json",
            success: function (data) {
                var index = parent.layer.getFrameIndex(window.name);  // 先得到当前iframe层的索引
                parent.layer.close(index);  // 再执行关闭
                parent.layui.table.reload(table_id);
                parent.layer.msg(data.msg, {time:1200});
            }, error: function (data) {
            }
        });
        return false; //阻止表单跳转。如果需要表单跳转，去掉这段即可。
    });
}

function form_on_submit_ajax(url_path, table_id, data) {
    layui.jquery.ajax({
        type: "POST",
        url: url_path,
        data: data.field,
        dataType: "json",
        success: function (data) {
            var index = parent.layer.getFrameIndex(window.name);  // 先得到当前iframe层的索引
            parent.layer.close(index);  // 再执行关闭
            parent.layui.table.reload(table_id);
            parent.layer.msg(data.msg, {time:1200});
        }, error: function (data) {
        }
    });
    return false; //阻止表单跳转。如果需要表单跳转，去掉这段即可。
}