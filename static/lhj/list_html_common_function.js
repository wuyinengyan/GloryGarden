// 表格加载渲染
function layui_table_render(table_prefix, table_cols, table_toolbar, table_height='full-160', table_where={}){
    layui.table.render({
        elem: '#table',  // 指定原始表格元素选择器（推荐id选择器）
        id: table_prefix + 'table',
        url: table_prefix + 'list',  // 数据接口
        height: table_height,
        cellMinWidth: 60,
        page: true,  // 开启分页
        loading: true,  // 加载条
        text: {none: '查无数据！'},
        defaultToolbar: ['filter', 'print', 'exports'],  // 默认操作行，只有三个
        toolbar: table_toolbar,
        cols: table_cols,
        where: table_where,
        response: {
            statusName: 'code',  // 规定数据状态的字段名称，默认：code
            statusCode: 0,  // 规定成功的状态码，默认：0
            msgName: 'msg',  // 规定状态信息的字段名称，默认：msg
            countName: 'count',  // 规定数据总数的字段名称，默认：count
            dataName: 'data',  // 规定数据列表的字段名称，默认：data
        },
    });
}


// 弹出框通用事件
function layer_open_common_event(obj, table_prefix, area, title='', content=''){
    let data = obj.data;  // 获得当前行数据
    let event_type = obj.event;  // 获得 lay-event 对应的值
    let iframe_id = table_prefix + event_type;
    let btn_id = 'save';

    if (event_type === 'info') {
        title = '查看';
    } else if (event_type === 'add') {
        title = '新增';
        content = iframe_id;
        layer_open_base_event(title, area, content, iframe_id, btn_id);
    } else if (event_type === 'edit') {
        title = '编辑';
        content = iframe_id + '?id=' + data.id;
        layer_open_base_event(title, area, content, iframe_id, btn_id);
    } else if (event_type === 'del') {
        title = '删除';
    } else{
        // 无
    }
}


// 弹出框基础事件
function layer_open_base_event(title, area, content, iframe_id, btn_id){
    layer.open({
        btn: ['确认', '取消'],
        yes: function (index, layero) {
            // #save为页面层提交按钮ID
            let submit = layero.find('#' + iframe_id + ' iframe').contents().find('#' + btn_id);
            submit.click();  //  触发提交监听
        },
        title: title
        ,id: iframe_id
        ,area: area
        ,content: content
        ,anim: 4  // 从左翻滚
        ,btnAlign: 'c'  // 按钮居中
        ,type: 2  // 类型iframe
        ,resize: true
        ,moveOut: true
        ,maxmin: true
        ,scrollbar: true
        ,shadeClose: false // 点击遮罩关闭层
        ,offset: '80px' // top、left:['100px', '200px']
    })
}