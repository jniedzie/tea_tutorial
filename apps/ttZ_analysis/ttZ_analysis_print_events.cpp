#include "ConfigManager.hpp"
#include "EventReader.hpp"
#include "ExtensionsHelpers.hpp"


int main(int argc, char **argv) {
  ConfigManager::Initialize(argv[1]);
  auto eventReader = std::make_shared<EventReader>();
 
  for (int iEvent = 0; iEvent < eventReader->GetNevents(); iEvent++) {
    auto event = eventReader->GetEvent(iEvent);
    auto muons = event->GetCollection("Muon");

    for (auto muon : *muons) {
      int pt = muon->Get("pt");
      info() << "Muon pt: " << pt << std::endl;
    }
  }
  return 0;
}
