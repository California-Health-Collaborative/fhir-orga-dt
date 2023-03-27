Class Python.ProductionCSV Extends Ens.Production
{

XData ProductionDefinition
{
<Production Name="Python.ProductionCSV" LogGeneralTraceEvents="false">
  <Description></Description>
  <ActorPoolSize>2</ActorPoolSize>
  <Item Name="Python.bs.ServiceCSV" Category="" ClassName="Python.bs.ServiceCSV" PoolSize="1" Enabled="true" Foreground="false" Comment="" LogTraceEvents="false" Schedule="">
  </Item>
  <Item Name="Python.bp.ProcessCSV" Category="" ClassName="Python.bp.ProcessCSV" PoolSize="1" Enabled="true" Foreground="false" Comment="" LogTraceEvents="false" Schedule="">
  </Item>
  <Item Name="Python.bo.FhirClient" Category="" ClassName="Python.bo.FhirClient" PoolSize="1" Enabled="true" Foreground="false" Comment="" LogTraceEvents="false" Schedule="">
  </Item>
</Production>
}

}
