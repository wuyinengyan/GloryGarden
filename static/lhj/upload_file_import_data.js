function upload_file(file, url_path) {
    let file_name = $("#import_file").val();
    alert(file_name);
    if (file_name === '') {
        layer.msg('请选择文件！', {time: 1300});
        return false;
    }

    //验证文件格式
    let file_type = (file_name.substring(file_name.lastIndexOf(".") + 1, file_name.length)).toLowerCase();
    if (file_type !== 'xls' && file_type !== 'xlxs') {
        layer.msg('文件格式不正确！', {time: 1300});
        return false;
    }

    //var index = layer.msg('正在上传，请稍候',{icon: 16,time:false,shade:0.8});
    // console.log(url_path);
    $.ajaxFileUpload({
        url: url_path, //用于文件上传的服务器端请求地址
        fileElementId: 'import_file',  // 需要上传的文件域的ID，即<input type="file">的ID。
        secureuri: false,  // 是否启用安全提交，默认为false。
        type: 'post',  // 当要提交自定义参数时，这个参数要设置成post
        dataType: 'json',  // 服务器返回的数据类型。可以为xml,script,json,html。如果不填写，jQuery会自动判断。
        async: true,
        success: function (data, res) {
            if (typeof (data.error) !== 'undefined') {
                if (data.error !== '') {
                    layer.msg(data.error);
                } else {
                    layer.msg(data.msg);
                }
            }
            layer.msg(res, function () {
                window.location.reload();
            });
        },
        error: function (data, status, e) {
            layer.msg("导入失败：" + e);
        }
    });
    return false;
}