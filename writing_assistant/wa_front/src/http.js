import axios from 'axios';

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'



const service = axios.create({
    baseURL: 'http://localhost:50000/', 
    
    timeout: 100000, 
})


service.interceptors.request.use(
    config => {
        
        return config
    },
    error => {

        console.log(error)
        return Promise.reject(error)
    }
)


service.interceptors.response.use(
    response => response,
    error => {
        console.log('err' + error) 
        return Promise.reject(error)
    }
)

export default service
// long-polling

// function getData() {
//     return service.get('/?min=0&max=100');
// }

// // create a promise that resolves after a short delay
// function delayPromise(ms) {
//     return new Promise(function (resolve) {
//         setTimeout(resolve, ms);
//     });
// }

// // cb is the callback function
// // interval is how often to poll
// // timeout is how long to poll waiting for a result (0 means try forever)
// function poll(cb, predicate, errorHandler, interval, timeout) {
//     let start = Date.now();

//     function run() {
//         return cb().then(function ({ data }) {
//             console.log('data:', data);
//             if (predicate(data)) {
//                 // we know we're done here, return from here whatever you
//                 // want the final resolved value of the promise to be
//                 return data;
//             } else {
//                 if (timeout !== 0 && Date.now() - start > timeout) {
//                     errorHandler();
//                 } else {
//                     // run again with a short delay
//                     return delayPromise(interval).then(run);
//                 }
//             }
//         });
//     }
//     return run();
// }

// function isGreaterThan90([number]) {
//     return number.random > 90;
// }

// function errorHandler() {
//     throw new Error('timeout error on poll');
// }

// function logResult(data) {
//     data = JSON.stringify(data, null, 2);
//     console.log(`result: ${data}`);
// }

// poll(getData, isGreaterThan90, errorHandler, 1000, 30 * 1000)
//     .then(logResult)
//     .catch(console.error);

// long-polling

