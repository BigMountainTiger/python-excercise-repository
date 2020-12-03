using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Net.Http;
using Newtonsoft.Json;

using Amazon.Lambda.Core;

[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.Json.JsonSerializer))]

namespace Word2pdf
{

  public class LambdaPayload {
    public string Payload { get; set; }
  }
  public class Function
  {
    public async Task<LambdaPayload> FunctionHandler(LambdaPayload input, ILambdaContext context)
    {
      var payload = await Task.Run(() => {
        return new LambdaPayload
        {
          Payload = input.Payload
        };
      });

      return payload;
    }
  }
}
