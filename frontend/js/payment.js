checkLogin();
const userId = localStorage.getItem("borrow_user");
const bookId = localStorage.getItem("borrow_book");

if (!userId || !bookId) {
    alert("No book selected for borrowing.");
    window.location.href = "books.html";
}
const userId = localStorage.getItem("borrow_user");

const bookId = localStorage.getItem("borrow_book");

const amount = 50;

async function pay(){

    try{

        showLoader();

        const payment={

            user_id:Number(userId),

            amount:amount,

            payment_method:document.getElementById("method").value

        };

        const result=await apiPost(

            "/payments/",

            payment

        );

        await apiPost(

            "/rentals/borrow",

            {

                user_id:Number(userId),

                book_id:Number(bookId),

                issue_date:new Date().toISOString().split("T")[0],

                due_date:new Date(

                    Date.now()+14*24*60*60*1000

                ).toISOString().split("T")[0]

            }

        );

        hideLoader();

        showToast(

            "Payment Successful"

        );

        setTimeout(()=>{

            alert(

                "Transaction ID : "+

                result.transaction_id

            );

            window.location.href="borrow.html";

        },1000);

    }

    catch(err){

        hideLoader();

        console.error(err);

        showToast(

            err.message,

            "error"

        );

    }

}