import scala.concurrent.duration._

import io.gatling.core.Predef._
import io.gatling.http.Predef._

class SlowAppSimulation extends Simulation {

  val httpProtocol = http
    .baseUrl("http://localhost:31313")

  val scn = scenario("Ping")
    .exec(
      http("Ping")
        .get("/ping")
    )

  setUp(
    scn.inject(
      constantUsersPerSec(1).during(60)
    )
  ).protocols(httpProtocol)
  
}