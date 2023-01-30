/**
 * @param {number[]} nums
 * @return {number[]}
 */
const buildArray = function (nums) {
    return nums.map(n=>nums[n]);
};

const inputs = [[0,2,1,5,3,4], [5,0,1,2,3,4]]
const outputs = [[0,1,2,4,5,3], [4,5,0,1,2,3]]
inputs.forEach((input,i)=>{
  const r = buildArray(input);
  if(JSON.stringify(r)!==JSON.stringify(outputs[i]))
      throw new Error('Failed: '+input+' ---- Got: '+JSON.stringify(r)+' !== '+JSON.stringify(outputs[i]));
  else console.log('Passed input: '+input);
});