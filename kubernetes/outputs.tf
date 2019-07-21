output "cluster-id" {
  value = "${digitalocean_kubernetes_cluster.project_digital_ocean_cluster.id}"
}

output "do_cluster_token_endpoint" {
  value = "${digitalocean_kubernetes_cluster.project_digital_ocean_cluster.endpoint}"
}

output "do_cluster_current_status" {
  value = "${digitalocean_kubernetes_cluster.project_digital_ocean_cluster.status}"
}

output "k8_ingress_object" {
  value = "${kubernetes_ingress.project-ingress-resource.load_balancer_ingress}"
}

# output "k8_ingress_publish_ip" {
#   value = "${kubernetes_ingress.project-ingress-resource.load_balancer_ingress.ip}"
# }

# output "k8_ingress" {
#   value = "${kubernetes_ingress.project-ingress-resource.load_balancer_ingress.hostname}"
# }
