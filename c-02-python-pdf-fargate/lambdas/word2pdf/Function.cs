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
    private string ConvertToPdf(string input) {
      string result = null;

      var input_bytes = System.Convert.FromBase64String(input);
      var input_stream = new System.IO.MemoryStream(input_bytes);
      var output_stream = new System.IO.MemoryStream();

      var pdfdoc = new Spire.Doc.Document(input_stream, Spire.Doc.FileFormat.Auto);
      pdfdoc.SaveToStream(output_stream, Spire.Doc.FileFormat.PDF);

      result = System.Convert.ToBase64String(output_stream.ToArray());
      return result;
    }

    public async Task<LambdaPayload> FunctionHandler(LambdaPayload input, ILambdaContext context)
    {
      System.Environment.SetEnvironmentVariable("FONTCONFIG_PATH", "/opt/lib");
      var payload = await Task.Run(() => {
        return new LambdaPayload
        {
          Payload = ConvertToPdf(input.Payload)
        };
      });

      return payload;
    }
  }
}
