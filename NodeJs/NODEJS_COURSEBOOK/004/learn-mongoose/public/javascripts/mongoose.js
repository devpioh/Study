document.querySelectorAll('#user-list tr').forEach( (el) =>
{
    el.addEventListener('click', () => 
    {
        var id = el.querySelector('td').textContent;
        getComment(id);
    });
});

// 사용자 로딩
function getUser()
{
    var xhr = new XMLHttpRequest();
    xhr.onload = () =>
    {
        if(200 === xhr.status)
        {
            var users = JSON.parse(xhr.responseText);
            console.log(users);

            var tbody = document.querySelector('#user-list tbody');
            tbody.innerHTML = '';

            users.map((user) => 
            {
                var row = document.createElement('tr');
                row.addEventListener('click', () =>
                {
                    getComment(user.id);
                });

                var td = document.createElement('td');
                td.textContent = user.id;
                row.appendChild(td);
                
                td = document.createElement('td');
                td.textContent = user.name;
                row.appendChild(td);

                td = document.createElement('td');
                td.textContent = user.age;
                row.appendChild(td);

                td = document.createElement('td');
                td.textContent = user.married ? '기혼' : '미혼';
                row.appendChild(td);

                tbody.appendChild(row);
            });
        }
        else
            console.error(xhr.responseText);
    };

    xhr.open('GET', '/users');
    xhr.send();
}

// 댓글 로딩
function getComment(id)
{
    var xhr = new XMLHttpRequest();
    xhr.onload = () =>
    {
        if( 200 == xhr.status )
        {
            var comments = JSON.parse(xhr.responseText);
            var tbody = document.querySelector('#comment-list tbody');
            tbody.innerHTML = '';

            comments.map( (comment) => 
            {
                var row = document.createElement('tr');

                var td = document.createElement('td');
                td.textContent = comment._id;
                row.appendChild(td);

                td = document.createElement('td');
                td.textContent = comment.commenter.name;
                row.appendChild(td);

                td = document.createElement('td');
                td.textContent = comment.comment;
                row.appendChild(td);

                var edit = document.createElement('button');
                edit.textContent = '수정';
                edit.addEventListener('click', () =>
                {
                    var newComment = prompt('바꿀 내용 입력');
                    if(!newComment)
                        return alert('내용은 반드시 입력하셔야 됩니다.');

                    var xhr = new XMLHttpRequest();
                    xhr.onload = () => 
                    {
                        if(200 === xhr.status)
                        {
                            console.log(xhr.responseText);
                            getComment(id);
                        }
                        else
                            console.error(xhr.responseText);
                    };
                    
                    xhr.open('PATCH', '/comments/' + comment._id);
                    xhr.setRequestHeader('Content-Type', 'application/json');
                    xhr.send(JSON.stringify({ comment: newComment }));
                });

                var remove = document.createElement('button');
                remove.textContent = '삭제';
                remove.addEventListener('click', () => 
                {
                    var xhr = new XMLHttpRequest();
                    xhr.onload = () => 
                    {
                        if(200 == xhr.status)
                        {
                            console.log(xhr.responseText);
                            getComment(id);
                        }
                        else
                            console.error(xhr.responseText);
                    };

                    xhr.open('DELETE', '/comments/' + comment._id);
                    xhr.send();
                });

                td = document.createElement('td');
                td.appendChild(edit);
                row.appendChild(td);

                td = document.createElement('td');
                td.appendChild(remove);
                row.appendChild(td);

                tbody.appendChild(row);
            });
        }
        else
            console.error(xhr.responseText);
    };

    xhr.open('GET', '/comments/' + id);
    xhr.send();
}

// 사용자 등록.
document.getElementById('user-form').addEventListener('submit', (e) => 
{
    e.preventDefault();
    
    var name = e.target.username.value;
    var age = e.target.age.value;
    var married = e.target.married.checked;

    if(!name)
        return alert('이름을 입력하세요.');

    if(!age)
        return alert('나이를 입력하세요.');
    
    var xhr = new XMLHttpRequest();
    xhr.onload = () => 
    {
        if(201 == xhr.status)
        {
            console.log(xhr.responseText);
            getUser();
        }
        else
            console.error(xhr.responseText);

    };

    xhr.open('POST', '/users');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({ name: name, age: age, married: married }));

    e.target.username.value = '';
    e.target.age.value = '';
    e.target.married.checked = false;
});


// 댓글 등록..
document.getElementById('comment-form').addEventListener('submit', (e) => 
{
    e.preventDefault();

    var id = e.target.userid.value;
    var comment = e.target.comment.value;

    if(!id)
        return alert('아이디를 입력하세요');
    
    if(!comment)
        return alert('댓글을 입력하세요');
    
    var xhr = new XMLHttpRequest();
    xhr.onload = () => 
    {
        if(201 == xhr.status)
        {
            console.log(xhr.responseText);
            getComment(id);
        }
        else
            console.error(xhr.responseText);
    };

    xhr.open('POST', '/comments');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({ id: id, comment: comment}));

    e.target.userid.value = '';
    e.target.comment.value = '';
});