
function onEdit(key)
{
     //click edit button
     var name = promt('select change name');
     if(!name)
     {
         return alert('plz select name');
     }

     var xhr = new XMLHttpRequest();
     xhr.onload = function ()
     {
         if( 200 === xhr.status )
             console.log(xhr.responseText);
         else 
             console.error(xhr.responseText);
     };
     xhr.open('PUT', '/users/'+key);
     xhr.setRequestHeader('Content-Type', 'application/json');
     xhr.send(JSON.stringify({name: name}));
}

function onDel(key)
{
    //click delete button
    var xhr = new XMLHttpRequest();
    xhr.onload = function ()
    {
        if(200 === xhr.status)
            console.log(xhr.responseText);
        else
            console.log(xhr.responseText);
    };
    xhr.open('DELETE', '/users/' + key);
    xhr.send();
}


function getUser()
{
    var xhr = new XMLHttpRequest();
    xhr.onload = function()
    {
        if( 200 === xhr.status )
        {
            var users = JSON.parse(xhr.responseText);
            var list = document.getElementById('list');
            list.innerHTML ='';

            Object.keys(users).map(function (key)
            {
                var userDiv = document.createElement('div');
                var span = document.createElement('span');
                span.textContent = users[key];
                
                var edit = document.createElement('button');
                edit.textContent = 'edit';
                //edit.addEventListener( 'click', onEdit(key)); 
                edit.addEventListener('click', function(){
                    //click edit button
                    var name = prompt('select change name');
                    if(!name)
                    {
                        return alert('plz select name');
                    }

                    var xhr = new XMLHttpRequest();
                    xhr.onload = function ()
                    {
                        if( 200 === xhr.status )
                            console.log(xhr.responseText);
                        else 
                            console.error(xhr.responseText);
                    };
                    xhr.open('PUT', '/users/'+key);
                    xhr.setRequestHeader('Content-Type', 'application/json');
                    xhr.send(JSON.stringify({name: name}));
                });

                var remove = document.createElement('button');
                remove.textContent = 'delete';
                //remove.addEventListener('click', onDel(key) );
                remove.addEventListener('click', function()
                {
                    //click delete button
                    var xhr = new XMLHttpRequest();
                    xhr.onload = function ()
                    {
                        if(200 === xhr.status)
                            console.log(xhr.responseText);
                        else
                            console.log(xhr.responseText);
                    };
                    xhr.open('DELETE', '/users/' + key);
                    xhr.send();
                });

                userDiv.appendChild(span);
                userDiv.appendChild(edit);
                userDiv.appendChild(remove);
                list.appendChild(userDiv);
            });
        }
        else
        {
            console.error(xhr.responseText);
        }
    };

    xhr.open('GET', '/users');
    xhr.send();
}

window.onload = getUser;

document.getElementById('form').addEventListener('submit', function(e)
{
    e.preventDefault();
    var name = e.target.username.value;
    if(!name)
    {
        return alert('input your name');
    }
    
    var xhr = new XMLHttpRequest();
    xhr.onload = function ()
    {
        if( 201 == xhr.status )
        {
            console.log(xhr.responseText);
            getUser();
        }
        else
        {
            console.error(xhr.responseText);
        }
    };
    xhr.open('POST', '/users');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({name: name}));
    e.target.username.value = '';
});