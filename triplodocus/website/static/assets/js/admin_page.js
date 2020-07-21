let ajoutForm = document.getElementById('form_ajout')

function displayBadges(deleteId, editId)
{
    document.getElementById(deleteId).style.visibility = 'visible';
    document.getElementById(editId).style.visibility = 'visible';
}
function hideBadges(deleteId, editId)
{
    document.getElementById(deleteId).style.visibility = 'hidden';
    document.getElementById(editId).style.visibility = 'hidden';

}

function showModalSuppression(id_to_delete)
{
    let target = id_to_delete.slice(13);
    document.getElementById("modal_suppression").className ="modal fade show";
    document.getElementById("modal_suppression").style.display ="block";

}

function deleteSong(id)
{
    console.log('salut')
    let body = {id: id}

    let host = window.location.origin;
    let delete_page = new URL('/delete_song',host)
    
    document.getElementById('button_supprimer').addEventListener('click',function(event)
    {
        fetch(delete_page,{
            method: 'POST',
            headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken':'{{csrf_token}}',
            'X-Requested-With':'XMLHttpRequest' 
            },

            body:JSON.stringify(body),
            mode:'cors',
            cache:'default',
            credentials:'include'     
        })
        .then((reponse)=>{
            document.getElementById('hide_span').click()
            document.getElementById(id + '_col').style.display = 'none'
        })
    })

}
ajoutForm.addEventListener('submit',function(event)
{
    let youtubeValue = document.getElementById('id_youtube')
    youtubeValue.value = youtubeValue.value.replace('watch?v=','embed/')
})

